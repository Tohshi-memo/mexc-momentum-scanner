# Decision Report

- generated_at: 2026-06-09T06:37:06.862138+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6119**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6119, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.06% | **-0.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.07% | **+0.04%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.04% | **+0.03%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.46% | **+1.46%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.01% | **+0.76%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.62% | **+0.73%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.15% | **+0.69%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$96.62** / 初期 $100.00 (-3.38%)
- 確定トレード: 11件 (TP 1 / SL 9 / EXP 1)
- 最新: SLX/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$154.23** / 初期 $100.00 (+54.23%)
- 確定: 1159件 (Win 289 / Loss 356 / Flat 514) / skip 1521件
- 成長率目線: 平均log +0.000374 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEST/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $154.23

## 4. Latest Market Context

- 更新: 2026-06-09T06:37:03.763604+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=63345.8
- Funnel: target 774 → liquid 155 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +51.05% | $25,017,494.42 |
| SLX/USDT:USDT | +29.40% | $1,620,971.90 |
| ZEST/USDT:USDT | +16.01% | $1,422,989.29 |
| POWER/USDT:USDT | +12.02% | $1,468,245.64 |
| SIREN/USDT:USDT | +10.27% | $11,222,949.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIPPIN/USDT:USDT | below_1h_threshold | +3.13% | +3.09% |
| SIREN/USDT:USDT | below_1h_threshold | +2.98% | +2.94% |
| ZEC/USDT:USDT | below_1h_threshold | +2.78% | +2.74% |
| LIT/USDT:USDT | below_1h_threshold | +2.32% | +2.28% |
| JTO/USDT:USDT | below_1h_threshold | +1.99% | +1.94% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

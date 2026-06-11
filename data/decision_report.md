# Decision Report

- generated_at: 2026-06-11T20:36:43.463023+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6404**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6404, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.09% | **+0.27%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| ASK | 20/20 | 100.0% | +0.13% | **+0.13%** |
| LIMIT_7PCT | 4/20 | 20.0% | -0.60% | **-0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.24% | **+1.24%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.29% | **+0.80%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +1.10% | **+0.73%** |
| LIMIT_FIB1272_LONG | 4/20 | 20.0% | +2.91% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$154.16** / 初期 $100.00 (+54.16%)
- 確定: 1321件 (Win 344 / Loss 422 / Flat 555) / skip 1644件
- 成長率目線: 平均log +0.000328 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SPACE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $154.16

## 4. Latest Market Context

- 更新: 2026-06-11T20:36:39.791716+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.41% price=63312.5
- Funnel: target 782 → liquid 160 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.3 >= 65=1, 4h RSI 75.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +96.20% | $117,326,817.82 |
| ESPORTS/USDT:USDT | +47.96% | $14,495,169.91 |
| NAORIS/USDT:USDT | +22.54% | $1,247,345.92 |
| UB/USDT:USDT | +16.08% | $1,678,075.49 |
| SKYAI/USDT:USDT | +12.07% | $12,379,140.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XPL/USDT:USDT | below_1h_threshold | +3.87% | +4.28% |
| ESPORTS/USDT:USDT | below_1h_threshold | +3.40% | +3.81% |
| UB/USDT:USDT | below_1h_threshold | +2.71% | +3.12% |
| BEAT/USDT:USDT | below_1h_threshold | +2.14% | +2.55% |
| ALLO/USDT:USDT | below_1h_threshold | +1.82% | +2.24% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

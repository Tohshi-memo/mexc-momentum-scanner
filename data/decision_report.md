# Decision Report

- generated_at: 2026-06-07T15:13:07.409052+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5968**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5968, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-2.11%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.11% | **-2.11%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +0.60% | **+0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +4.78% | **+3.11%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +4.86% | **+2.92%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +3.87% | **+2.71%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +4.76% | **+1.67%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.92% | **+1.34%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 5件 (TP 1 / SL 4 / EXP 0)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$148.82** / 初期 $100.00 (+48.82%)
- 確定: 1085件 (Win 264 / Loss 327 / Flat 494) / skip 1444件
- 成長率目線: 平均log +0.000366 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: WLD/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $148.82

## 4. Latest Market Context

- 更新: 2026-06-07T15:13:01.560460+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=61799.7
- Funnel: target 768 → liquid 122 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BSB/USDT:USDT | +72.64% | $11,042,310.80 |
| FIDA/USDT:USDT | +66.96% | $9,307,228.37 |
| SIREN/USDT:USDT | +60.91% | $24,352,342.15 |
| BLESS/USDT:USDT | +41.95% | $5,855,642.12 |
| LAB/USDT:USDT | +40.51% | $63,136,572.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| B/USDT:USDT | below_1h_threshold | +2.64% | +2.76% |
| FIDA/USDT:USDT | below_1h_threshold | +2.00% | +2.12% |
| WLD/USDT:USDT | below_1h_threshold | +1.53% | +1.64% |
| LAB/USDT:USDT | below_1h_threshold | +1.08% | +1.19% |
| BEAT/USDT:USDT | below_1h_threshold | +0.66% | +0.78% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

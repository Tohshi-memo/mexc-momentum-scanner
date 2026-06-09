# Decision Report

- generated_at: 2026-06-09T19:58:10.587819+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6160**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6160, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.66% | **+0.07%** |
| LIMIT_5PCT | 4/20 | 20.0% | -0.29% | **-0.06%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |
| LIMIT_6PCT | 2/20 | 10.0% | -1.06% | **-0.11%** |
| LIMIT_3PCT | 15/20 | 75.0% | -0.18% | **-0.13%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.61% | **+0.88%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.17% | **+0.59%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.85% | **+0.51%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +4.93% | **+0.49%** |

## 2. $100 Live Portfolio

- 残高: **$95.66** / 初期 $100.00 (-4.34%)
- 確定トレード: 13件 (TP 1 / SL 11 / EXP 1)
- 最新: PIPPIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.66
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$148.01** / 初期 $100.00 (+48.01%)
- 確定: 1188件 (Win 297 / Loss 374 / Flat 517) / skip 1533件
- 成長率目線: 平均log +0.000330 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EPIC/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $148.01

## 4. Latest Market Context

- 更新: 2026-06-09T19:58:04.786267+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.47% price=62047.1
- Funnel: target 778 → liquid 156 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HOME/USDT:USDT | +22.16% | $3,835,466.55 |
| BTW/USDT:USDT | +18.34% | $5,594,152.75 |
| STG/USDT:USDT | +10.41% | $1,225,805.85 |
| OPN/USDT:USDT | +9.30% | $2,572,201.39 |
| BLESS/USDT:USDT | +8.83% | $4,481,579.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STG/USDT:USDT | below_1h_threshold | +4.84% | +4.37% |
| JCT/USDT:USDT | below_1h_threshold | +3.27% | +2.81% |
| NEAR/USDT:USDT | below_1h_threshold | +2.41% | +1.94% |
| IO/USDT:USDT | below_1h_threshold | +1.43% | +0.96% |
| POL/USDT:USDT | below_1h_threshold | +1.19% | +0.72% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

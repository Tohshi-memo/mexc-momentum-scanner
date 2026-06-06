# Decision Report

- generated_at: 2026-06-06T02:56:42.999960+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5775**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5775, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 14/20 | 70.0% | -0.29% | **-0.20%** |
| ASK | 20/20 | 100.0% | -0.27% | **-0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +2.00% | **+1.20%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.74% | **+1.04%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.06% | **+0.74%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.63% | **+0.38%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.77% | **+0.35%** |

## 2. $100 Live Portfolio

- 残高: **$99.03** / 初期 $100.00 (-0.97%)
- 確定トレード: 100件 (TP 31 / SL 66 / EXP 3)
- 最新: OPG/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.03
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$130.54** / 初期 $100.00 (+30.54%)
- 確定: 1012件 (Win 239 / Loss 313 / Flat 460) / skip 1324件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +7.25%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ZEST/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $130.54

## 4. Latest Market Context

- 更新: 2026-06-06T02:56:37.491026+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=60988.3
- Funnel: target 771 → liquid 159 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.4 >= 65=1, 4h RSI 87.0 >= 65=1, 4h RSI 68.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HOME/USDT:USDT | +26.24% | $5,471,053.36 |
| VELVET/USDT:USDT | +25.58% | $1,973,833.91 |
| BTW/USDT:USDT | +21.51% | $33,060,753.41 |
| CLO/USDT:USDT | +19.55% | $1,615,633.15 |
| OPN/USDT:USDT | +18.87% | $23,920,065.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EPIC/USDT:USDT | below_1h_threshold | +4.83% | +4.90% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.22% | +2.28% |
| HOME/USDT:USDT | below_1h_threshold | +2.15% | +2.21% |
| OPN/USDT:USDT | below_1h_threshold | +2.07% | +2.13% |
| ORDI/USDT:USDT | below_1h_threshold | +1.15% | +1.21% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

# Decision Report

- generated_at: 2026-09-10T17:56:47.173867+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14175**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14175, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.01% | **+0.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.11% | **+0.78%** |
| LIMIT_BB3S | 2/15 | 13.3% | +5.50% | **+0.73%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +5.42% | **+0.54%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.27% | **+0.51%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +4.76% | **+4.76%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.95% | **+0.67%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.29% | **+0.64%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.45% | **+0.40%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +0.40% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 208件 (TP 78 / SL 125 / EXP 5)
- 最新: EIGEN/USDT:USDT SL_HIT PnL -3.25% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,074.20** / 初期 $100.00 (+974.20%)
- 確定: 5355件 (Win 1611 / Loss 1729 / Flat 2015) / skip 5381件
- 成長率目線: 平均log +0.000443 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EIGEN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,074.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$208.18** / 初期 $100.00 (+108.18%)
- 確定: 2769件 (Win 765 / Loss 649 / Flat 1355) / skip 4817件
- 成長率目線: 平均log +0.000265 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1025 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EIGEN/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $208.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.69** / 初期 $100.00 (+22.69%)
- 確定: 2680件 (Win 791 / Loss 1023 / Flat 866) / pending 6件 / skip 2963件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000456 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: EIGEN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $122.69

## 6. Latest Market Context

- 更新: 2026-09-10T17:56:26.158396+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=77336.1
- Funnel: target 1067 → liquid 177 → pre 50 → checked 50 → surge 5 → strict 4
- Surge前reject: below_1h_threshold=45, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CNPY/USDT:USDT | +28.10% | $1,102,876.63 |
| NIULAI/USDT:USDT | +12.99% | $1,464,854.71 |
| PONS/USDT:USDT | +11.29% | $8,944,278.60 |
| 4STOCK/USDT:USDT | +10.29% | $2,477,369.60 |
| EIGEN/USDT:USDT | +9.81% | $1,362,913.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MEMEROBINHOOD/USDT:USDT | below_1h_threshold | +4.50% | +4.29% |
| SOPH/USDT:USDT | below_1h_threshold | +4.38% | +4.17% |
| PONS/USDT:USDT | below_1h_threshold | +3.70% | +3.49% |
| CATE/USDT:USDT | below_1h_threshold | +3.21% | +2.99% |
| BTW/USDT:USDT | below_1h_threshold | +2.85% | +2.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

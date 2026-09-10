# Decision Report

- generated_at: 2026-09-10T18:56:25.041848+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14180**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14180, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.01% | **+0.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +1.89% | **+0.57%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_BB3S | 3/13 | 23.1% | +2.33% | **+0.54%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +3.56% | **+0.53%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/6 | 100.0% | +3.30% | **+3.30%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.50% | **+0.27%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.30% | **+0.19%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.37% | **+0.17%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.18% | **+0.15%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 208件 (TP 78 / SL 125 / EXP 5)
- 最新: EIGEN/USDT:USDT SL_HIT PnL -3.25% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,058.17** / 初期 $100.00 (+958.17%)
- 確定: 5360件 (Win 1611 / Loss 1732 / Flat 2017) / skip 5381件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIULAI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $1,058.17

## 4. Robust Adaptive DryRun ($100)

- 残高: **$208.08** / 初期 $100.00 (+108.08%)
- 確定: 2774件 (Win 767 / Loss 650 / Flat 1357) / skip 4817件
- 成長率目線: 平均log +0.000264 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0912 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $208.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.05** / 初期 $100.00 (+22.05%)
- 確定: 2685件 (Win 791 / Loss 1026 / Flat 868) / pending 3件 / skip 2963件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000378 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $122.05

## 6. Latest Market Context

- 更新: 2026-09-10T18:56:09.446643+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=77211.8
- Funnel: target 1067 → liquid 177 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +28.57% | $1,789,555.98 |
| CNPY/USDT:USDT | +15.78% | $1,594,274.65 |
| EIGEN/USDT:USDT | +9.46% | $1,951,359.26 |
| PONS/USDT:USDT | +9.05% | $9,057,288.14 |
| MEMEROBINHOOD/USDT:USDT | +8.31% | $1,029,604.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MEMEROBINHOOD/USDT:USDT | below_1h_threshold | +3.63% | +3.75% |
| BTR/USDT:USDT | below_1h_threshold | +2.92% | +3.04% |
| USELESS/USDT:USDT | below_1h_threshold | +2.88% | +2.99% |
| RAVE/USDT:USDT | below_1h_threshold | +2.64% | +2.75% |
| VVV/USDT:USDT | below_1h_threshold | +2.25% | +2.37% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

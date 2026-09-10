# Decision Report

- generated_at: 2026-09-10T20:51:26.084051+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14187**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=14187, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.54%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.54% | **-1.54%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 3/20 | 15.0% | +3.56% | **+0.53%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.45% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 8/8 | 100.0% | +2.52% | **+2.52%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +2.75% | **+1.79%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.33% | **+0.93%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.21% | **+0.88%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 208件 (TP 78 / SL 125 / EXP 5)
- 最新: EIGEN/USDT:USDT SL_HIT PnL -3.25% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,053.34** / 初期 $100.00 (+953.34%)
- 確定: 5363件 (Win 1612 / Loss 1734 / Flat 2017) / skip 5385件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NIULAI/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.55% 残高後 $1,053.34

## 4. Robust Adaptive DryRun ($100)

- 残高: **$208.08** / 初期 $100.00 (+108.08%)
- 確定: 2781件 (Win 767 / Loss 650 / Flat 1364) / skip 4817件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0715 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RAY/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $208.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.58** / 初期 $100.00 (+22.58%)
- 確定: 2692件 (Win 794 / Loss 1028 / Flat 870) / pending 4件 / skip 2963件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000255 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RAY/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $122.58

## 6. Latest Market Context

- 更新: 2026-09-10T20:51:13.522138+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=77223.0
- Funnel: target 1067 → liquid 174 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +41.56% | $3,717,190.08 |
| CNPY/USDT:USDT | +17.22% | $1,931,185.03 |
| MARSCOIN/USDT:USDT | +12.40% | $2,426,727.03 |
| 4STOCK/USDT:USDT | +10.62% | $2,385,667.34 |
| EIGEN/USDT:USDT | +10.10% | $2,943,145.65 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MARSCOIN/USDT:USDT | below_relative_strength | +5.05% | +4.93% |
| CHIP/USDT:USDT | below_1h_threshold | +4.67% | +4.55% |
| APT/USDT:USDT | below_1h_threshold | +3.69% | +3.57% |
| RAY/USDT:USDT | below_1h_threshold | +3.48% | +3.37% |
| NES/USDT:USDT | below_1h_threshold | +2.56% | +2.44% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

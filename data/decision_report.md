# Decision Report

- generated_at: 2026-09-11T02:16:18.343624+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14193**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.27% / filled 20/20。**
- 全期間 MARKET基準: n=14193, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.27%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.27% | **+0.27%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.27% | **+0.27%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.14% | **+0.06%** |
| LIMIT_4PCT | 11/20 | 55.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 6/6 | 100.0% | +0.84% | **+0.84%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.44% | **+0.40%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.43% | **+0.30%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.22% | **+0.13%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 208件 (TP 78 / SL 125 / EXP 5)
- 最新: EIGEN/USDT:USDT SL_HIT PnL -3.25% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,057.44** / 初期 $100.00 (+957.44%)
- 確定: 5366件 (Win 1613 / Loss 1735 / Flat 2018) / skip 5388件
- 成長率目線: 平均log +0.000440 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EIGEN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.24% 残高後 $1,057.44

## 4. Robust Adaptive DryRun ($100)

- 残高: **$208.08** / 初期 $100.00 (+108.08%)
- 確定: 2787件 (Win 767 / Loss 650 / Flat 1370) / skip 4817件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0157 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EIGEN/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $208.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$122.25** / 初期 $100.00 (+22.25%)
- 確定: 2697件 (Win 795 / Loss 1031 / Flat 871) / pending 4件 / skip 2963件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000185 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: NIULAI/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $122.25

## 6. Latest Market Context

- 更新: 2026-09-11T02:16:08.190564+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=76911.5
- Funnel: target 1067 → liquid 170 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NIULAI/USDT:USDT | +32.66% | $7,607,961.22 |
| RAY/USDT:USDT | +18.34% | $6,762,411.44 |
| CNPY/USDT:USDT | +16.38% | $2,641,219.93 |
| PONS/USDT:USDT | +12.21% | $7,982,473.31 |
| NES/USDT:USDT | +10.04% | $2,014,410.96 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CNPY/USDT:USDT | below_1h_threshold | +4.13% | +4.18% |
| NES/USDT:USDT | below_1h_threshold | +3.35% | +3.39% |
| RAY/USDT:USDT | below_1h_threshold | +3.06% | +3.10% |
| NIULAI/USDT:USDT | below_1h_threshold | +2.91% | +2.96% |
| PONS/USDT:USDT | below_1h_threshold | +1.50% | +1.54% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

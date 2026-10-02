# Decision Report

- generated_at: 2026-10-02T13:36:31.675081+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15999**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15999, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.59% | **-0.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.03% | **+0.71%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +1.03% | **+0.26%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.13% | **+0.10%** |
| LIMIT_BB3S | 2/11 | 18.2% | -0.34% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 12/20 | 60.0% | +1.36% | **+0.82%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.74% | **+0.56%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.22% | **+0.43%** |
| LIMIT_BB3S_LONG | 3/8 | 37.5% | +1.06% | **+0.40%** |
| MARKET_LONG | 20/20 | 100.0% | +0.39% | **+0.39%** |

## 2. $100 Live Portfolio

- 残高: **$120.27** / 初期 $100.00 (+20.27%)
- 確定トレード: 229件 (TP 82 / SL 140 / EXP 7)
- 最新: SI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.27
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,339.32** / 初期 $100.00 (+1239.32%)
- 確定: 6104件 (Win 1806 / Loss 1960 / Flat 2338) / skip 6456件
- 成長率目線: 平均log +0.000425 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: APE/USDT:USDT `LIMIT_FIB1272` TP_HIT account +1.00% 残高後 $1,339.32

## 4. Robust Adaptive DryRun ($100)

- 残高: **$275.42** / 初期 $100.00 (+175.42%)
- 確定: 3605件 (Win 1005 / Loss 844 / Flat 1756) / skip 5805件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score +0.0074 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $275.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4162件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000062 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-02T13:36:18.250138+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.21% price=86954.1
- Funnel: target 1098 → liquid 175 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +81.14% | $4,183,321.63 |
| SAND/USDT:USDT | +57.08% | $42,916,437.66 |
| MAGMA/USDT:USDT | +24.49% | $2,594,747.04 |
| ENJ/USDT:USDT | +23.69% | $1,518,165.34 |
| NIGHT/USDT:USDT | +23.51% | $7,972,242.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BATON/USDT:USDT | below_1h_threshold | +4.29% | +4.08% |
| SOXL/USDT:USDT | below_1h_threshold | +3.77% | +3.55% |
| ETHFI/USDT:USDT | below_1h_threshold | +3.51% | +3.30% |
| KORU/USDT:USDT | below_1h_threshold | +3.31% | +3.10% |
| MONAD/USDT:USDT | below_1h_threshold | +2.87% | +2.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

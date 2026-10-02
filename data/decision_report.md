# Decision Report

- generated_at: 2026-10-02T22:31:14.279470+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16022**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16022, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.95%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.95% | **-0.95%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +1.74% | **+0.78%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.06% | **+0.74%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |
| LIMIT_BB3S | 4/15 | 26.7% | +1.39% | **+0.37%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.60% | **+1.56%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.21% | **+1.09%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.94% | **+0.87%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +1.64% | **+0.74%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.88% | **+0.61%** |

## 2. $100 Live Portfolio

- 残高: **$120.27** / 初期 $100.00 (+20.27%)
- 確定トレード: 229件 (TP 82 / SL 140 / EXP 7)
- 最新: SI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.27
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,335.42** / 初期 $100.00 (+1235.42%)
- 確定: 6127件 (Win 1807 / Loss 1963 / Flat 2357) / skip 6456件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MAGMA/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,335.42

## 4. Robust Adaptive DryRun ($100)

- 残高: **$275.42** / 初期 $100.00 (+175.42%)
- 確定: 3605件 (Win 1005 / Loss 844 / Flat 1756) / skip 5828件
- 成長率目線: 平均log +0.000281 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0323 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SI/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $275.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4179件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000171 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-02T22:31:04.531355+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=84481.8
- Funnel: target 1099 → liquid 177 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +21.98% | $3,326,648.34 |
| LONGXIA/USDT:USDT | +8.18% | $17,266,161.59 |
| NIGHT/USDT:USDT | +4.23% | $7,832,286.48 |
| NMR/USDT:USDT | +3.46% | $2,273,826.45 |
| SAND/USDT:USDT | +3.43% | $69,090,952.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIGHT/USDT:USDT | below_1h_threshold | +1.65% | +1.66% |
| LONGXIA/USDT:USDT | below_1h_threshold | +1.48% | +1.50% |
| VELVET/USDT:USDT | below_1h_threshold | +1.10% | +1.11% |
| SAND/USDT:USDT | below_1h_threshold | +1.09% | +1.10% |
| ONE/USDT:USDT | below_1h_threshold | +1.03% | +1.04% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

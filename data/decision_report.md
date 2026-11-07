# Decision Report

- generated_at: 2026-11-07T04:06:30.926731+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18351**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18351, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.97%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.97% | **-1.97%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +1.30% | **+0.45%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_BB3S | 3/18 | 16.7% | +0.91% | **+0.15%** |
| LIMIT_6PCT | 7/20 | 35.0% | +0.20% | **+0.07%** |
| LIMIT_7PCT | 4/20 | 20.0% | -0.60% | **-0.12%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.99% | **+2.00%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +3.16% | **+1.89%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +4.84% | **+1.69%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.98% | **+1.29%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +2.39% | **+0.96%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 264件 (TP 97 / SL 159 / EXP 8)
- 最新: CSOPSKHYNIX2L/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,485.91** / 初期 $100.00 (+1385.91%)
- 確定: 7047件 (Win 2026 / Loss 2248 / Flat 2773) / skip 7865件
- 成長率目線: 平均log +0.000383 / 幾何平均 +0.038% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LYN/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $1,485.91

## 4. Robust Adaptive DryRun ($100)

- 残高: **$390.18** / 初期 $100.00 (+290.18%)
- 確定: 4717件 (Win 1269 / Loss 1039 / Flat 2409) / skip 7045件
- 成長率目線: 平均log +0.000289 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0612 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ARIA/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $390.18

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6511件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000177 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-07T04:06:14.919956+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=75865.0
- Funnel: target 1089 → liquid 154 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AIN/USDT:USDT | +41.97% | $5,006,751.57 |
| AKE/USDT:USDT | +32.80% | $61,543,018.88 |
| LYN/USDT:USDT | +18.04% | $1,767,889.22 |
| ONE/USDT:USDT | +17.85% | $14,563,244.48 |
| JCT/USDT:USDT | +17.19% | $4,867,179.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONE/USDT:USDT | below_1h_threshold | +4.49% | +4.48% |
| MUU/USDT:USDT | below_1h_threshold | +1.17% | +1.16% |
| BTW/USDT:USDT | below_1h_threshold | +1.15% | +1.14% |
| JCT/USDT:USDT | below_1h_threshold | +1.11% | +1.10% |
| MVLL/USDT:USDT | below_1h_threshold | +1.04% | +1.03% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

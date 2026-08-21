# Decision Report

- generated_at: 2026-08-21T23:51:25.075316+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12274**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12274, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.06% | **+0.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_8PCT | 4/20 | 20.0% | +8.00% | **+1.60%** |
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.19% | **+0.55%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.36% | **+1.18%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.09% | **+0.98%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +2.40% | **+0.84%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.11% | **+0.83%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +3.27% | **+0.65%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 190件 (TP 72 / SL 113 / EXP 5)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$675.59** / 初期 $100.00 (+575.59%)
- 確定: 4394件 (Win 1345 / Loss 1439 / Flat 1610) / skip 4441件
- 成長率目線: 平均log +0.000435 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_7PCT` TP_HIT account +1.00% 残高後 $675.59

## 4. Robust Adaptive DryRun ($100)

- 残高: **$154.75** / 初期 $100.00 (+54.75%)
- 確定: 1880件 (Win 518 / Loss 449 / Flat 913) / skip 3805件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1402 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $154.75

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.30** / 初期 $100.00 (+17.30%)
- 確定: 1825件 (Win 541 / Loss 693 / Flat 591) / pending 2件 / skip 1921件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000313 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_7PCT` TP_HIT account +0.34% 残高後 $117.30

## 6. Latest Market Context

- 更新: 2026-08-21T23:51:13.761551+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.33% price=78178.4
- Funnel: target 1018 → liquid 217 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.4 >= 65=1, 4h RSI 94.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BASECAT/USDT:USDT | +217.11% | $3,051,988.28 |
| CATE/USDT:USDT | +69.51% | $11,349,203.13 |
| JIMOTHY/USDT:USDT | +20.54% | $1,628,881.63 |
| MAGMA/USDT:USDT | +17.48% | $2,698,848.12 |
| AGI/USDT:USDT | +16.03% | $1,566,725.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MAGMA/USDT:USDT | below_1h_threshold | +2.99% | +3.32% |
| ETC/USDT:USDT | below_1h_threshold | +2.72% | +3.05% |
| AGI/USDT:USDT | below_1h_threshold | +1.69% | +2.02% |
| AR/USDT:USDT | below_1h_threshold | +1.59% | +1.92% |
| H/USDT:USDT | below_1h_threshold | +1.49% | +1.82% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

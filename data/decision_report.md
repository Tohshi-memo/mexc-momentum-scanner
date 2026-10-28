# Decision Report

- generated_at: 2026-10-28T20:41:22.434467+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17736**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17736, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.02% | **+0.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 11/20 | 55.0% | +2.02% | **+1.11%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.81% | **+0.49%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.33% | **+0.27%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.63% | **+0.50%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |
| MARKET_LONG | 20/20 | 100.0% | +0.29% | **+0.29%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.13% | **+0.23%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.15% | **+0.09%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 255件 (TP 94 / SL 153 / EXP 8)
- 最新: BTW/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,546.79** / 初期 $100.00 (+1446.79%)
- 確定: 6780件 (Win 1971 / Loss 2171 / Flat 2638) / skip 7517件
- 成長率目線: 平均log +0.000404 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ORCLSTOCK/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $1,546.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$359.08** / 初期 $100.00 (+259.08%)
- 確定: 4257件 (Win 1155 / Loss 969 / Flat 2133) / skip 6890件
- 成長率目線: 平均log +0.000300 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0406 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ORCLSTOCK/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $359.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5895件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000192 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-28T20:41:09.609171+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.58% price=81075.0
- Funnel: target 1083 → liquid 166 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| XPIN/USDT:USDT | +35.05% | $1,657,142.87 |
| AKE/USDT:USDT | +19.03% | $6,602,164.66 |
| Q/USDT:USDT | +13.61% | $27,104,493.95 |
| INIT/USDT:USDT | +9.72% | $1,966,207.07 |
| BEAT/USDT:USDT | +7.66% | $11,208,516.75 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XPIN/USDT:USDT | below_1h_threshold | +4.92% | +5.50% |
| Q/USDT:USDT | below_1h_threshold | +4.69% | +5.26% |
| AGT/USDT:USDT | below_1h_threshold | +3.25% | +3.83% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +3.11% | +3.69% |
| SI/USDT:USDT | below_1h_threshold | +2.56% | +3.14% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

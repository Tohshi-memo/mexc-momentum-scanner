# Decision Report

- generated_at: 2026-08-29T14:16:16.928843+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12947**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12947, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 6/20 | 30.0% | +1.89% | **+0.57%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.22% | **+0.10%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +4.83% | **+1.45%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.65% | **+1.32%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +5.11% | **+1.02%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$728.11** / 初期 $100.00 (+628.11%)
- 確定: 4717件 (Win 1429 / Loss 1548 / Flat 1740) / skip 4791件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 4/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $728.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$161.06** / 初期 $100.00 (+61.06%)
- 確定: 2031件 (Win 556 / Loss 487 / Flat 988) / skip 4327件
- 成長率目線: 平均log +0.000235 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0721 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: 4/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $161.06

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.05** / 初期 $100.00 (+15.05%)
- 確定: 2037件 (Win 597 / Loss 794 / Flat 646) / pending 0件 / skip 2378件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000210 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.05

## 6. Latest Market Context

- 更新: 2026-08-29T14:16:05.944197+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=77646.5
- Funnel: target 1023 → liquid 137 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TOAD/USDT:USDT | +85.45% | $2,112,140.70 |
| HNT/USDT:USDT | +79.18% | $11,742,729.42 |
| 4/USDT:USDT | +50.92% | $4,674,320.71 |
| NIL/USDT:USDT | +30.01% | $4,983,006.81 |
| O/USDT:USDT | +17.25% | $1,654,353.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +4.82% | +4.85% |
| HNT/USDT:USDT | below_1h_threshold | +3.07% | +3.10% |
| DASH/USDT:USDT | below_1h_threshold | +2.56% | +2.59% |
| DEXE/USDT:USDT | below_1h_threshold | +1.38% | +1.41% |
| CYS/USDT:USDT | below_1h_threshold | +1.17% | +1.20% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

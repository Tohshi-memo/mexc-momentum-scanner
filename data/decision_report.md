# Decision Report

- generated_at: 2026-08-29T11:16:14.740996+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **12931**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=12931, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.39% | **-0.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +2.79% | **+0.98%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | -1.76% | **-0.26%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.79% | **+1.79%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.63% | **+1.30%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +0.13% | **+0.06%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$725.74** / 初期 $100.00 (+625.74%)
- 確定: 4701件 (Win 1424 / Loss 1544 / Flat 1733) / skip 4791件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: 4/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $725.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$160.40** / 初期 $100.00 (+60.40%)
- 確定: 2015件 (Win 551 / Loss 486 / Flat 978) / skip 4327件
- 成長率目線: 平均log +0.000234 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0631 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: 4/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $160.40

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.07** / 初期 $100.00 (+16.07%)
- 確定: 2026件 (Win 595 / Loss 785 / Flat 646) / pending 2件 / skip 2372件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000342 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 4/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.07

## 6. Latest Market Context

- 更新: 2026-08-29T11:16:05.571359+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=77693.8
- Funnel: target 1023 → liquid 140 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HNT/USDT:USDT | +100.27% | $7,133,660.10 |
| TOAD/USDT:USDT | +95.22% | $1,826,363.10 |
| 4/USDT:USDT | +39.96% | $2,047,783.79 |
| O/USDT:USDT | +18.73% | $1,434,538.73 |
| LONGXIA/USDT:USDT | +18.13% | $2,060,492.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +2.25% | +2.13% |
| TOAD/USDT:USDT | below_1h_threshold | +1.75% | +1.64% |
| VELVET/USDT:USDT | below_1h_threshold | +1.69% | +1.58% |
| NIL/USDT:USDT | below_1h_threshold | +1.55% | +1.43% |
| O/USDT:USDT | below_1h_threshold | +1.24% | +1.13% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

# Decision Report

- generated_at: 2026-08-30T05:01:23.030525+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13021**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13021, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.35% | **-2.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 9/20 | 45.0% | +1.26% | **+0.57%** |
| LIMIT_BB3S | 11/17 | 64.7% | +0.85% | **+0.55%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.60% | **+0.48%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.34% | **+0.28%** |
| LIMIT_4PCT | 17/20 | 85.0% | +0.24% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +4.70% | **+2.35%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +5.51% | **+2.20%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +4.32% | **+2.16%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +3.77% | **+1.51%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.00% | **+1.33%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$792.09** / 初期 $100.00 (+692.09%)
- 確定: 4791件 (Win 1460 / Loss 1575 / Flat 1756) / skip 4791件
- 成長率目線: 平均log +0.000432 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HNT/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $792.09

## 4. Robust Adaptive DryRun ($100)

- 残高: **$173.90** / 初期 $100.00 (+73.90%)
- 確定: 2105件 (Win 589 / Loss 513 / Flat 1003) / skip 4327件
- 成長率目線: 平均log +0.000263 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0609 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HNT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $173.90

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.33** / 初期 $100.00 (+17.33%)
- 確定: 2064件 (Win 607 / Loss 800 / Flat 657) / pending 2件 / skip 2425件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000365 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HNT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $117.33

## 6. Latest Market Context

- 更新: 2026-08-30T05:01:08.278448+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=78083.1
- Funnel: target 1023 → liquid 116 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HNT/USDT:USDT | +75.85% | $30,526,773.37 |
| FONE/USDT:USDT | +66.59% | $1,360,513.24 |
| NIULAI/USDT:USDT | +60.58% | $2,462,651.23 |
| PONS/USDT:USDT | +40.50% | $1,504,275.00 |
| PROM/USDT:USDT | +31.32% | $14,550,695.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BICO/USDT:USDT | below_1h_threshold | +0.44% | +0.44% |
| SKR/USDT:USDT | below_1h_threshold | +0.43% | +0.43% |
| BTR/USDT:USDT | below_1h_threshold | +0.35% | +0.35% |
| TUT/USDT:USDT | below_1h_threshold | +0.34% | +0.34% |
| PONS/USDT:USDT | below_1h_threshold | +0.31% | +0.31% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

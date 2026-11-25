# Decision Report

- generated_at: 2026-11-25T23:41:21.118952+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19652**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19652, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.24%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.24% | **-1.24%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.49% | **+0.24%** |
| LIMIT_6PCT | 2/20 | 10.0% | -1.06% | **-0.11%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.19% | **-0.14%** |
| LIMIT_5PCT | 2/20 | 10.0% | -1.52% | **-0.15%** |
| LIMIT_BB3S | 2/19 | 10.5% | -2.83% | **-0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.34% | **+1.34%** |
| LIMIT_FIB1272_LONG | 5/20 | 25.0% | +2.69% | **+0.67%** |
| LIMIT_5PCT_LONG | 6/20 | 30.0% | +2.14% | **+0.64%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.15% | **+0.62%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 288件 (TP 105 / SL 175 / EXP 8)
- 最新: SOXS/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,988.31** / 初期 $100.00 (+1888.31%)
- 確定: 7612件 (Win 2191 / Loss 2450 / Flat 2971) / skip 8601件
- 成長率目線: 平均log +0.000393 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: KOR/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,988.31

## 4. Robust Adaptive DryRun ($100)

- 残高: **$467.28** / 初期 $100.00 (+367.28%)
- 確定: 5220件 (Win 1389 / Loss 1124 / Flat 2707) / skip 7843件
- 成長率目線: 平均log +0.000295 / 幾何平均 +0.030% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KIMCHI/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.09% 残高後 $467.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7817件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000274 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-25T23:41:10.960061+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.36% price=60309.4
- Funnel: target 1097 → liquid 152 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BULLA/USDT:USDT | +30.72% | $1,324,123.82 |
| SOXL/USDT:USDT | +25.40% | $1,893,962,811.73 |
| MANTRA/USDT:USDT | +21.36% | $3,820,920.78 |
| SNXX/USDT:USDT | +19.13% | $35,338,257.23 |
| KORU/USDT:USDT | +19.03% | $104,360,660.84 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| GUA/USDT:USDT | below_1h_threshold | +4.99% | +4.63% |
| SOXL/USDT:USDT | below_1h_threshold | +1.97% | +1.61% |
| NVDL/USDT:USDT | below_1h_threshold | +1.93% | +1.57% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +1.92% | +1.56% |
| MMT/USDT:USDT | below_1h_threshold | +1.59% | +1.22% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

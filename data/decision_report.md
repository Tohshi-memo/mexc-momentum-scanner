# Decision Report

- generated_at: 2026-11-12T06:26:25.176115+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18720**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.93% / filled 20/20。**
- 全期間 MARKET基準: n=18720, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+2.93%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.93% | **+2.93%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.93% | **+2.93%** |
| LIMIT_1PCT | 15/20 | 75.0% | +1.70% | **+1.27%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.81% | **+1.18%** |
| LIMIT_2PCT | 12/20 | 60.0% | +1.02% | **+0.61%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 2/20 | 10.0% | -1.45% | **-0.15%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | -0.44% | **-0.20%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | -0.79% | **-0.24%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | -1.24% | **-0.62%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | -0.84% | **-0.80%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 273件 (TP 99 / SL 166 / EXP 8)
- 最新: IDOL/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,708.40** / 初期 $100.00 (+1608.40%)
- 確定: 7233件 (Win 2083 / Loss 2316 / Flat 2834) / skip 8048件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SNXX/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,708.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$390.28** / 初期 $100.00 (+290.28%)
- 確定: 4779件 (Win 1283 / Loss 1057 / Flat 2439) / skip 7352件
- 成長率目線: 平均log +0.000285 / 幾何平均 +0.028% per trade / maxDD +4.29%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0204 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AGT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $390.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6877件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000215 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-12T06:26:11.763137+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.20% price=73700.6
- Funnel: target 1103 → liquid 146 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KGEN/USDT:USDT | +16.20% | $1,086,041.38 |
| SOXS/USDT:USDT | +10.36% | $64,218,746.50 |
| AGT/USDT:USDT | +6.11% | $37,324,511.44 |
| Q/USDT:USDT | +6.11% | $4,501,393.07 |
| SQQQ/USDT:USDT | +3.59% | $2,137,192.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KGEN/USDT:USDT | below_1h_threshold | +3.58% | +3.38% |
| Q/USDT:USDT | below_1h_threshold | +2.24% | +2.04% |
| SOXS/USDT:USDT | below_1h_threshold | +1.54% | +1.34% |
| PIEVERSE/USDT:USDT | below_1h_threshold | +1.39% | +1.19% |
| ZEC/USDT:USDT | below_1h_threshold | +0.92% | +0.72% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

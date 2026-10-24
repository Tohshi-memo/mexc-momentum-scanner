# Decision Report

- generated_at: 2026-10-24T13:01:10.075827+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17366**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17366, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 9/20 | 45.0% | +3.32% | **+1.49%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_5PCT | 11/20 | 55.0% | +2.16% | **+1.19%** |
| LIMIT_8PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +3.59% | **+2.52%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +2.25% | **+2.02%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.35% | **+1.76%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +1.53% | **+0.84%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.45% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,359.25** / 初期 $100.00 (+1259.25%)
- 確定: 6619件 (Win 1915 / Loss 2108 / Flat 2596) / skip 7308件
- 成長率目線: 平均log +0.000394 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ORDER/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,359.25

## 4. Robust Adaptive DryRun ($100)

- 残高: **$298.55** / 初期 $100.00 (+198.55%)
- 確定: 3930件 (Win 1083 / Loss 920 / Flat 1927) / skip 6847件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1530 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BIRB/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $298.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5524件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000516 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-24T13:01:01.193137+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=80755.1
- Funnel: target 1079 → liquid 147 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ORDER/USDT:USDT | +121.84% | $7,856,922.33 |
| BMT/USDT:USDT | +50.76% | $2,287,508.68 |
| BIRB/USDT:USDT | +25.02% | $12,812,702.74 |
| IN/USDT:USDT | +5.91% | $1,189,367.52 |
| NIL/USDT:USDT | +4.80% | $2,329,330.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IN/USDT:USDT | below_1h_threshold | +2.24% | +2.23% |
| BMT/USDT:USDT | below_1h_threshold | +1.32% | +1.31% |
| AGT/USDT:USDT | below_1h_threshold | +0.50% | +0.49% |
| KORU/USDT:USDT | below_1h_threshold | +0.48% | +0.46% |
| ORDER/USDT:USDT | below_1h_threshold | +0.40% | +0.39% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

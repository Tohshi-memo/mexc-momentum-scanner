# Decision Report

- generated_at: 2026-07-22T20:11:20.433332+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9316**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9316, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.23% | **-0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +6.86% | **+1.03%** |
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.87% | **+0.43%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.87% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +2.34% | **+2.11%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.46% | **+1.39%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.50% | **+1.05%** |
| LIMIT_FIB1272_LONG | 7/19 | 36.8% | +1.85% | **+0.68%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.15% | **+0.63%** |

## 2. $100 Live Portfolio

- 残高: **$105.37** / 初期 $100.00 (+5.37%)
- 確定トレード: 133件 (TP 45 / SL 83 / EXP 5)
- 最新: DEXE/USDT:USDT SL_HIT PnL -4.00% 残高後 $105.37
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$425.06** / 初期 $100.00 (+325.06%)
- 確定: 3301件 (Win 1040 / Loss 1064 / Flat 1197) / skip 2576件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AEHRSTOCK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $425.06

## 4. Robust Adaptive DryRun ($100)

- 残高: **$130.36** / 初期 $100.00 (+30.36%)
- 確定: 1161件 (Win 312 / Loss 254 / Flat 595) / skip 1566件
- 成長率目線: 平均log +0.000228 / 幾何平均 +0.023% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0846 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BANK/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $130.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.37** / 初期 $100.00 (+1.37%)
- 確定: 426件 (Win 142 / Loss 177 / Flat 107) / pending 2件 / skip 366件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000251 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $101.37

## 6. Latest Market Context

- 更新: 2026-07-22T20:11:13.821272+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=65785.3
- Funnel: target 890 → liquid 182 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +16.79% | $3,832,116.72 |
| BANK/USDT:USDT | +15.60% | $101,948,691.67 |
| BROCCOLIF3B/USDT:USDT | +14.44% | $1,686,214.88 |
| ON/USDT:USDT | +12.03% | $1,558,706.70 |
| RIF/USDT:USDT | +7.01% | $3,934,499.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ON/USDT:USDT | below_1h_threshold | +2.41% | +2.57% |
| ACE/USDT:USDT | below_1h_threshold | +1.78% | +1.94% |
| RIF/USDT:USDT | below_1h_threshold | +1.69% | +1.85% |
| ZAMA/USDT:USDT | below_1h_threshold | +1.47% | +1.63% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +1.05% | +1.21% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

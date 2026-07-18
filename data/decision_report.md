# Decision Report

- generated_at: 2026-07-18T00:56:21.989105+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8904**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.18% / filled 20/20。**
- 全期間 MARKET基準: n=8904, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.18%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.18% | **+1.18%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.18% | **+1.18%** |
| LIMIT_6PCT | 5/20 | 25.0% | +3.15% | **+0.79%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.21% | **+0.49%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.95% | **+0.47%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +2.78% | **+1.25%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.64% | **+1.07%** |
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +1.07% | **+0.80%** |
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.58% | **+0.49%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +0.60% | **+0.48%** |

## 2. $100 Live Portfolio

- 残高: **$112.37** / 初期 $100.00 (+12.37%)
- 確定トレード: 113件 (TP 43 / SL 66 / EXP 4)
- 最新: CASHCAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $112.37
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$367.56** / 初期 $100.00 (+267.56%)
- 確定: 3019件 (Win 939 / Loss 959 / Flat 1121) / skip 2446件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SYN/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.24% 残高後 $367.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$111.86** / 初期 $100.00 (+11.86%)
- 確定: 866件 (Win 204 / Loss 175 / Flat 487) / skip 1449件
- 成長率目線: 平均log +0.000129 / 幾何平均 +0.013% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0691 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $111.86

## 5. Causal Adaptive DryRun ($100)

- 残高: **$99.65** / 初期 $100.00 (-0.35%)
- 確定: 162件 (Win 52 / Loss 86 / Flat 24) / pending 4件 / skip 209件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000165 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_7PCT` SL_HIT account +0.12% 残高後 $99.65

## 6. Latest Market Context

- 更新: 2026-07-18T00:56:12.351092+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=63872.1
- Funnel: target 885 → liquid 172 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.2 >= 65=1, 4h RSI 71.1 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +59.76% | $10,807,331.39 |
| AKE/USDT:USDT | +16.10% | $49,301,604.84 |
| CASHCAT/USDT:USDT | +14.89% | $1,230,599.89 |
| SYN/USDT:USDT | +14.01% | $4,962,828.51 |
| BANK/USDT:USDT | +11.40% | $21,717,499.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PI/USDT:USDT | below_1h_threshold | +3.17% | +3.22% |
| PENGU/USDT:USDT | below_1h_threshold | +1.15% | +1.20% |
| INJ/USDT:USDT | below_1h_threshold | +1.11% | +1.16% |
| US/USDT:USDT | below_1h_threshold | +1.10% | +1.16% |
| CRO/USDT:USDT | below_1h_threshold | +1.01% | +1.06% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

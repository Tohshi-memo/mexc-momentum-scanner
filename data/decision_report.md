# Decision Report

- generated_at: 2026-07-15T12:56:31.196385+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8740**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8740, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.03% | **-1.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 10/20 | 50.0% | +5.24% | **+2.62%** |
| LIMIT_8PCT | 9/20 | 45.0% | +5.71% | **+2.57%** |
| LIMIT_9PCT | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_6PCT | 11/20 | 55.0% | +1.95% | **+1.07%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +3.62% | **+2.90%** |
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +4.16% | **+2.78%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +3.59% | **+2.70%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.38% | **+2.20%** |
| MARKET_LONG | 20/20 | 100.0% | +1.73% | **+1.73%** |

## 2. $100 Live Portfolio

- 残高: **$103.73** / 初期 $100.00 (+3.73%)
- 確定トレード: 98件 (TP 34 / SL 62 / EXP 2)
- 最新: MAGMA/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.73
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$342.63** / 初期 $100.00 (+242.63%)
- 確定: 2879件 (Win 901 / Loss 935 / Flat 1043) / skip 2422件
- 成長率目線: 平均log +0.000428 / 幾何平均 +0.043% per trade / maxDD +8.13%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RAVE/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.82% 残高後 $342.63

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.51** / 初期 $100.00 (+6.51%)
- 確定: 706件 (Win 167 / Loss 165 / Flat 374) / skip 1445件
- 成長率目線: 平均log +0.000089 / 幾何平均 +0.009% per trade / maxDD +3.89%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.1512 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $106.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$98.75** / 初期 $100.00 (-1.25%)
- 確定: 61件 (Win 19 / Loss 39 / Flat 3) / pending 3件 / skip 152件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000388 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 0G/USDT:USDT `LIMIT_7PCT` EXPIRED account +0.00% 残高後 $98.75

## 6. Latest Market Context

- 更新: 2026-07-15T12:56:23.083662+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.58% price=65080.3
- Funnel: target 871 → liquid 170 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.0 >= 65=1, 4h RSI 75.8 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +231.34% | $21,629,310.19 |
| US/USDT:USDT | +37.82% | $5,618,137.50 |
| DODO/USDT:USDT | +36.83% | $11,590,546.79 |
| AEHRSTOCK/USDT:USDT | +35.62% | $4,118,961.03 |
| 0G/USDT:USDT | +20.41% | $2,050,883.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| US/USDT:USDT | below_1h_threshold | +3.52% | +2.94% |
| TAC/USDT:USDT | below_1h_threshold | +2.62% | +2.05% |
| XLM/USDT:USDT | below_1h_threshold | +2.38% | +1.81% |
| INJ/USDT:USDT | below_1h_threshold | +2.32% | +1.74% |
| ETH/USDT:USDT | below_1h_threshold | +2.26% | +1.69% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

# Decision Report

- generated_at: 2026-07-26T01:46:16.303804+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9553**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9553, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.77%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.77% | **-0.77%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.65% | **+0.26%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.15% | **-0.01%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.80% | **+2.24%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.03% | **+1.93%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.34% | **+0.93%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.64% | **+0.90%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$467.54** / 初期 $100.00 (+367.54%)
- 確定: 3381件 (Win 1076 / Loss 1096 / Flat 1209) / skip 2733件
- 成長率目線: 平均log +0.000456 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RIF/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $467.54

## 4. Robust Adaptive DryRun ($100)

- 残高: **$139.94** / 初期 $100.00 (+39.94%)
- 確定: 1206件 (Win 336 / Loss 266 / Flat 604) / skip 1758件
- 成長率目線: 平均log +0.000279 / 幾何平均 +0.028% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1243 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $139.94

## 5. Causal Adaptive DryRun ($100)

- 残高: **$109.34** / 初期 $100.00 (+9.34%)
- 確定: 597件 (Win 204 / Loss 228 / Flat 165) / pending 1件 / skip 424件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000577 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $109.34

## 6. Latest Market Context

- 更新: 2026-07-26T01:46:09.324734+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=64443.9
- Funnel: target 898 → liquid 119 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.3 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EUL/USDT:USDT | +51.03% | $28,593,049.17 |
| BANK/USDT:USDT | +21.81% | $89,224,916.27 |
| VELVET/USDT:USDT | +15.29% | $8,013,240.61 |
| ESPORTS/USDT:USDT | +14.36% | $29,269,184.65 |
| LIGHT/USDT:USDT | +10.35% | $1,026,035.83 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +3.22% | +3.28% |
| LIGHT/USDT:USDT | below_1h_threshold | +2.84% | +2.90% |
| BANK/USDT:USDT | below_1h_threshold | +1.49% | +1.55% |
| RAVE/USDT:USDT | below_1h_threshold | +1.44% | +1.50% |
| ORDI/USDT:USDT | below_1h_threshold | +1.07% | +1.13% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

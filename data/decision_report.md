# Decision Report

- generated_at: 2026-11-08T09:36:27.986274+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18427**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18427, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_FIB1272 | 12/20 | 60.0% | +1.24% | **+0.75%** |
| LIMIT_9PCT | 7/20 | 35.0% | +0.66% | **+0.23%** |
| LIMIT_BB3S | 4/15 | 26.7% | +0.86% | **+0.23%** |
| LIMIT_8PCT | 7/20 | 35.0% | +0.53% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +4.22% | **+4.22%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.35% | **+2.12%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +3.57% | **+1.96%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.59% | **+1.81%** |
| LIMIT_5PCT_LONG | 7/20 | 35.0% | +4.69% | **+1.64%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 265件 (TP 97 / SL 160 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,617.09** / 初期 $100.00 (+1517.09%)
- 確定: 7123件 (Win 2049 / Loss 2273 / Flat 2801) / skip 7865件
- 成長率目線: 平均log +0.000391 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JCT/USDT:USDT `LIMIT_3PCT_LONG` TP_HIT account +1.00% 残高後 $1,617.09

## 4. Robust Adaptive DryRun ($100)

- 残高: **$389.21** / 初期 $100.00 (+289.21%)
- 確定: 4755件 (Win 1277 / Loss 1047 / Flat 2431) / skip 7083件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0204 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CLAUDIA/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $389.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6590件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000438 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-08T09:36:14.668482+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=75881.1
- Funnel: target 1089 → liquid 103 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CLAUDIA/USDT:USDT | +301.16% | $11,819,863.57 |
| JCT/USDT:USDT | +34.76% | $3,329,638.82 |
| KOMA/USDT:USDT | +31.23% | $1,250,778.14 |
| AIOT/USDT:USDT | +11.80% | $2,724,309.89 |
| ICNT/USDT:USDT | +9.52% | $4,247,628.46 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONE/USDT:USDT | below_1h_threshold | +1.99% | +2.01% |
| ANTHROPIC/USDT:USDT | below_1h_threshold | +1.33% | +1.36% |
| ICNT/USDT:USDT | below_1h_threshold | +1.10% | +1.13% |
| LIT/USDT:USDT | below_1h_threshold | +0.50% | +0.53% |
| ZEC/USDT:USDT | below_1h_threshold | +0.24% | +0.26% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

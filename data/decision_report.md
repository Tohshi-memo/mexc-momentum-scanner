# Decision Report

- generated_at: 2026-11-11T15:21:30.041761+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18686**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18686, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-2.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.80% | **-2.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +3.93% | **+0.79%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +2.51% | **+0.63%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.88% | **+0.44%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +3.21% | **+3.21%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +3.61% | **+3.07%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +3.74% | **+1.68%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.95% | **+1.62%** |
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |

## 2. $100 Live Portfolio

- 残高: **$120.89** / 初期 $100.00 (+20.89%)
- 確定トレード: 270件 (TP 97 / SL 165 / EXP 8)
- 最新: SNXX/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.89
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,730.11** / 初期 $100.00 (+1630.11%)
- 確定: 7218件 (Win 2079 / Loss 2307 / Flat 2832) / skip 8029件
- 成長率目線: 平均log +0.000395 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AGT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,730.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$391.65** / 初期 $100.00 (+291.65%)
- 確定: 4778件 (Win 1283 / Loss 1056 / Flat 2439) / skip 7319件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1408 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JCT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $391.65

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6847件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000278 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-11T15:21:15.978062+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=73536.9
- Funnel: target 1103 → liquid 143 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.6 >= 65=1, 4h RSI 65.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +141.70% | $22,286,192.87 |
| SNXX/USDT:USDT | +30.68% | $38,075,301.85 |
| MUU/USDT:USDT | +26.19% | $12,994,388.31 |
| ARIA/USDT:USDT | +21.15% | $8,764,385.89 |
| CRWVSTOCK/USDT:USDT | +20.23% | $6,962,309.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AXTISTOCK/USDT:USDT | below_1h_threshold | +3.46% | +3.47% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +3.09% | +3.09% |
| JCT/USDT:USDT | below_1h_threshold | +2.96% | +2.97% |
| MUU/USDT:USDT | below_1h_threshold | +2.84% | +2.84% |
| CRWVSTOCK/USDT:USDT | below_1h_threshold | +2.49% | +2.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

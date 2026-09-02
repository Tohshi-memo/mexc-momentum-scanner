# Decision Report

- generated_at: 2026-09-02T16:16:31.628145+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13347**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13347, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-2.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.09% | **-2.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.27% | **+0.51%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +3.13% | **+2.66%** |
| LIMIT_BB3S_LONG | 4/4 | 100.0% | +2.62% | **+2.62%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.85% | **+1.92%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.87% | **+1.72%** |
| MARKET_LONG | 20/20 | 100.0% | +1.49% | **+1.49%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 198件 (TP 74 / SL 119 / EXP 5)
- 最新: FONE/USDT:USDT TP_HIT PnL +8.00% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$846.82** / 初期 $100.00 (+746.82%)
- 確定: 4973件 (Win 1506 / Loss 1629 / Flat 1838) / skip 4935件
- 成長率目線: 平均log +0.000430 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BULLA/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $846.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$178.99** / 初期 $100.00 (+78.99%)
- 確定: 2326件 (Win 651 / Loss 556 / Flat 1119) / skip 4432件
- 成長率目線: 平均log +0.000250 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1043 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BULLA/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +0.69% 残高後 $178.99

## 5. Causal Adaptive DryRun ($100)

- 残高: **$114.78** / 初期 $100.00 (+14.78%)
- 確定: 2093件 (Win 611 / Loss 819 / Flat 663) / pending 0件 / skip 2729件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000321 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $114.78

## 6. Latest Market Context

- 更新: 2026-09-02T16:16:23.459219+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=77302.7
- Funnel: target 1044 → liquid 163 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 75.1 >= 65=1, 4h RSI 88.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| USELESS/USDT:USDT | +10.27% | $27,527,308.44 |
| BULLA/USDT:USDT | +6.01% | $1,432,593.05 |
| NIULAI/USDT:USDT | +4.65% | $2,513,646.59 |
| MARSCOIN/USDT:USDT | +3.69% | $3,289,673.39 |
| EGLD/USDT:USDT | +2.73% | $2,976,663.39 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIULAI/USDT:USDT | below_1h_threshold | +4.20% | +4.13% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +3.69% | +3.63% |
| EGLD/USDT:USDT | below_1h_threshold | +2.80% | +2.73% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +2.24% | +2.17% |
| FLOCK/USDT:USDT | below_1h_threshold | +1.83% | +1.76% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

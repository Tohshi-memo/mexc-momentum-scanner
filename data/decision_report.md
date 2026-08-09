# Decision Report

- generated_at: 2026-08-09T01:21:16.399348+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10906**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10906, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.81%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.81% | **-0.81%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.60% | **+0.46%** |
| LIMIT_9PCT | 4/20 | 20.0% | +1.15% | **+0.23%** |
| LIMIT_8PCT | 4/20 | 20.0% | +0.93% | **+0.19%** |
| LIMIT_10PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_1PCT | 19/20 | 95.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +2.56% | **+0.77%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.85% | **+0.72%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.20% | **+0.60%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.10% | **+0.38%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$649.28** / 初期 $100.00 (+549.28%)
- 確定: 3907件 (Win 1228 / Loss 1271 / Flat 1408) / skip 3560件
- 成長率目線: 平均log +0.000479 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $649.28

## 4. Robust Adaptive DryRun ($100)

- 残高: **$142.00** / 初期 $100.00 (+42.00%)
- 確定: 1511件 (Win 424 / Loss 360 / Flat 727) / skip 2806件
- 成長率目線: 平均log +0.000232 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0174 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $142.00

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.44** / 初期 $100.00 (+17.44%)
- 確定: 1248件 (Win 390 / Loss 480 / Flat 378) / pending 0件 / skip 1132件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000072 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CAP/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account -0.10% 残高後 $117.44

## 6. Latest Market Context

- 更新: 2026-08-09T01:21:08.715870+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=64947.4
- Funnel: target 961 → liquid 149 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 97.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TUT/USDT:USDT | +68.51% | $24,712,073.52 |
| COOKIE/USDT:USDT | +32.75% | $3,662,158.19 |
| BLUAI/USDT:USDT | +23.52% | $7,440,997.44 |
| BTW/USDT:USDT | +16.01% | $15,655,927.35 |
| SAGA/USDT:USDT | +14.77% | $1,245,028.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLUAI/USDT:USDT | below_1h_threshold | +3.53% | +3.54% |
| BEAT/USDT:USDT | below_1h_threshold | +3.50% | +3.50% |
| CAP/USDT:USDT | below_1h_threshold | +3.17% | +3.18% |
| GWEI/USDT:USDT | below_1h_threshold | +2.19% | +2.20% |
| XAI/USDT:USDT | below_1h_threshold | +1.15% | +1.16% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

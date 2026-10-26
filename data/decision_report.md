# Decision Report

- generated_at: 2026-10-26T22:41:26.709956+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17527**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17527, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.20% | **-0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 5/20 | 25.0% | +5.60% | **+1.40%** |
| LIMIT_6PCT | 11/20 | 55.0% | +2.50% | **+1.38%** |
| LIMIT_BB3S | 5/12 | 41.7% | +3.20% | **+1.33%** |
| LIMIT_8PCT | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.69% | **+1.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +2.74% | **+2.47%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +2.33% | **+1.87%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.43% | **+1.36%** |
| LIMIT_BB3S_LONG | 4/8 | 50.0% | +1.44% | **+0.72%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.16% | **+0.69%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 252件 (TP 93 / SL 151 / EXP 8)
- 最新: Q/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,526.92** / 初期 $100.00 (+1426.92%)
- 確定: 6721件 (Win 1956 / Loss 2152 / Flat 2613) / skip 7367件
- 成長率目線: 平均log +0.000406 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: Q/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,526.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$322.25** / 初期 $100.00 (+222.25%)
- 確定: 4056件 (Win 1118 / Loss 953 / Flat 1985) / skip 6882件
- 成長率目線: 平均log +0.000289 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0669 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: Q/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $322.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5691件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000327 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-26T22:41:12.123709+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.16% price=79941.0
- Funnel: target 1078 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 78.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| Q/USDT:USDT | +203.14% | $18,764,362.65 |
| DODO/USDT:USDT | +6.42% | $1,357,725.19 |
| AGT/USDT:USDT | +5.51% | $1,745,028.35 |
| DNA/USDT:USDT | +4.30% | $1,209,984.99 |
| BAT/USDT:USDT | +2.94% | $2,245,060.91 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DODO/USDT:USDT | below_1h_threshold | +2.88% | +3.04% |
| ORDER/USDT:USDT | below_1h_threshold | +1.82% | +1.98% |
| AGT/USDT:USDT | below_1h_threshold | +1.49% | +1.65% |
| BULLA/USDT:USDT | below_1h_threshold | +1.47% | +1.63% |
| BAT/USDT:USDT | below_1h_threshold | +1.12% | +1.28% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

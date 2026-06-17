# Decision Report

- generated_at: 2026-06-17T12:11:02.471793+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6930**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6930, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| ASK | 20/20 | 100.0% | +0.32% | **+0.32%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/11 | 63.6% | +2.80% | **+1.78%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +1.95% | **+0.88%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.78% | **+0.66%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.61% | **+0.42%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.83% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$195.81** / 初期 $100.00 (+95.81%)
- 確定: 1802件 (Win 489 / Loss 567 / Flat 746) / skip 1689件
- 成長率目線: 平均log +0.000373 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SIREN/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $195.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$101.55** / 初期 $100.00 (+1.55%)
- 確定: 203件 (Win 48 / Loss 44 / Flat 111) / skip 138件
- 成長率目線: 平均log +0.000076 / 幾何平均 +0.008% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1247 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SIREN/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $101.55

## 5. Latest Market Context

- 更新: 2026-06-17T12:10:56.166284+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=64831.4
- Funnel: target 786 → liquid 165 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +67.59% | $9,158,734.23 |
| AGT/USDT:USDT | +55.08% | $1,130,508.40 |
| HIGH/USDT:USDT | +39.45% | $3,355,792.62 |
| BP/USDT:USDT | +24.29% | $1,040,065.12 |
| ID/USDT:USDT | +23.27% | $1,550,110.30 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HIGH/USDT:USDT | below_relative_strength | +5.03% | +4.94% |
| BP/USDT:USDT | below_1h_threshold | +2.92% | +2.83% |
| BLESS/USDT:USDT | below_1h_threshold | +2.37% | +2.29% |
| MYX/USDT:USDT | below_1h_threshold | +2.31% | +2.22% |
| ESPORTS/USDT:USDT | below_1h_threshold | +2.02% | +1.94% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

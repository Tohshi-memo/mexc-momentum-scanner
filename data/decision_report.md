# Decision Report

- generated_at: 2026-06-18T00:27:28.538832+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6983**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6983, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.15%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.15% | **-1.15%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.35% | **+0.54%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.24% | **+0.16%** |
| LIMIT_2PCT | 18/20 | 90.0% | -0.21% | **-0.19%** |
| LIMIT_8PCT | 8/20 | 40.0% | -0.57% | **-0.23%** |
| LIMIT_10PCT | 6/20 | 30.0% | -0.85% | **-0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +2.90% | **+2.90%** |
| MARKET_LONG | 20/20 | 100.0% | +2.00% | **+2.00%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.60% | **+1.12%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.87% | **+0.93%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.38% | **+0.76%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$206.76** / 初期 $100.00 (+106.76%)
- 確定: 1830件 (Win 503 / Loss 576 / Flat 751) / skip 1714件
- 成長率目線: 平均log +0.000397 / 幾何平均 +0.040% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $206.76

## 4. Robust Adaptive DryRun ($100)

- 残高: **$104.46** / 初期 $100.00 (+4.46%)
- 確定: 256件 (Win 69 / Loss 65 / Flat 122) / skip 138件
- 成長率目線: 平均log +0.000170 / 幾何平均 +0.017% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0994 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $104.46

## 5. Latest Market Context

- 更新: 2026-06-18T00:27:23.416103+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=64524.8
- Funnel: target 790 → liquid 174 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +128.35% | $23,177,705.68 |
| O/USDT:USDT | +77.30% | $1,476,122.31 |
| SYN/USDT:USDT | +44.04% | $4,242,986.18 |
| RE/USDT:USDT | +16.70% | $1,854,448.41 |
| H/USDT:USDT | +15.29% | $38,329,080.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| US/USDT:USDT | below_1h_threshold | +4.30% | +4.22% |
| ID/USDT:USDT | below_1h_threshold | +4.28% | +4.21% |
| BEAT/USDT:USDT | below_1h_threshold | +4.14% | +4.07% |
| PLAY/USDT:USDT | below_1h_threshold | +2.92% | +2.84% |
| STG/USDT:USDT | below_1h_threshold | +2.89% | +2.81% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

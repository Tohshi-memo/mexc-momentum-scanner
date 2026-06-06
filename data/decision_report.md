# Decision Report

- generated_at: 2026-06-06T23:23:06.881361+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5908**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5908, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| ASK | 20/20 | 100.0% | +0.29% | **+0.29%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +6.54% | **+4.67%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.14% | **+0.97%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.82% | **+0.53%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.68% | **+0.24%** |
| MARKET_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$99.00** / 初期 $100.00 (-1.00%)
- 確定トレード: 2件 (TP 0 / SL 2 / EXP 0)
- 最新: PORTAL/USDT:USDT SL_HIT PnL -4.00% 残高後 $99.00
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$137.07** / 初期 $100.00 (+37.07%)
- 確定: 1038件 (Win 249 / Loss 319 / Flat 470) / skip 1431件
- 成長率目線: 平均log +0.000304 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_BB3S_LONG` TP_HIT account +1.00% 残高後 $137.07

## 4. Latest Market Context

- 更新: 2026-06-06T23:23:03.852570+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.23% price=60649.2
- Funnel: target 771 → liquid 130 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +40.15% | $64,685,833.17 |
| FIDA/USDT:USDT | +38.25% | $2,831,789.50 |
| SKYAI/USDT:USDT | +32.42% | $27,251,992.25 |
| BTW/USDT:USDT | +22.58% | $13,057,591.97 |
| EDEN/USDT:USDT | +14.19% | $1,066,168.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BLESS/USDT:USDT | below_1h_threshold | +3.43% | +3.20% |
| FIDA/USDT:USDT | below_1h_threshold | +3.07% | +2.85% |
| BABY/USDT:USDT | below_1h_threshold | +2.24% | +2.02% |
| SIREN/USDT:USDT | below_1h_threshold | +2.08% | +1.86% |
| SLX/USDT:USDT | below_1h_threshold | +2.03% | +1.81% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

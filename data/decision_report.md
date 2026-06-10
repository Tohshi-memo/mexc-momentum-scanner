# Decision Report

- generated_at: 2026-06-10T22:32:43.670321+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6274**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6274, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.01% | **-1.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 11/20 | 55.0% | +1.14% | **+0.63%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.80% | **+0.56%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.43% | **+0.36%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.44% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.10% | **+1.10%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +2.01% | **+1.01%** |
| MARKET_LONG | 20/20 | 100.0% | +0.81% | **+0.81%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.55% | **+0.70%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.35% | **+0.61%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$150.45** / 初期 $100.00 (+50.45%)
- 確定: 1260件 (Win 317 / Loss 394 / Flat 549) / skip 1575件
- 成長率目線: 平均log +0.000324 / 幾何平均 +0.032% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SKYAI/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $150.45

## 4. Latest Market Context

- 更新: 2026-06-10T22:32:40.442287+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.07% price=61370.5
- Funnel: target 785 → liquid 153 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +72.88% | $34,425,437.33 |
| STRAX/USDT:USDT | +17.90% | $1,254,144.82 |
| BEAT/USDT:USDT | +15.89% | $172,925,358.60 |
| FOLKS/USDT:USDT | +5.25% | $12,045,303.15 |
| POWER/USDT:USDT | +5.21% | $1,477,002.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STRAX/USDT:USDT | below_1h_threshold | +3.54% | +3.47% |
| STG/USDT:USDT | below_1h_threshold | +2.94% | +2.87% |
| XMR/USDT:USDT | below_1h_threshold | +1.27% | +1.20% |
| BSB/USDT:USDT | below_1h_threshold | +1.03% | +0.96% |
| SIREN/USDT:USDT | below_1h_threshold | +1.01% | +0.94% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

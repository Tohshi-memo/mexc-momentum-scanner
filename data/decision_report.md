# Decision Report

- generated_at: 2026-06-11T00:27:21.976589+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6284**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6284, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 13/20 | 65.0% | +1.87% | **+1.22%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_7PCT | 5/20 | 25.0% | +2.80% | **+0.70%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +3.19% | **+0.64%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +2.80% | **+1.96%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.46% | **+1.60%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +2.14% | **+1.28%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.41% | **+1.13%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$95.18** / 初期 $100.00 (-4.82%)
- 確定トレード: 14件 (TP 1 / SL 12 / EXP 1)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.18
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$147.45** / 初期 $100.00 (+47.45%)
- 確定: 1270件 (Win 319 / Loss 401 / Flat 550) / skip 1575件
- 成長率目線: 平均log +0.000306 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $147.45

## 4. Latest Market Context

- 更新: 2026-06-11T00:27:18.745448+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.60% price=61847.8
- Funnel: target 785 → liquid 155 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 71.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +90.25% | $42,740,694.03 |
| BEAT/USDT:USDT | +26.63% | $187,461,903.88 |
| FIGHT/USDT:USDT | +15.33% | $1,036,347.44 |
| UAI/USDT:USDT | +14.25% | $2,156,579.83 |
| STRAX/USDT:USDT | +10.96% | $1,269,746.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +4.56% | +3.97% |
| AVNT/USDT:USDT | below_1h_threshold | +3.46% | +2.86% |
| STG/USDT:USDT | below_1h_threshold | +2.99% | +2.40% |
| DRAM/USDT:USDT | below_1h_threshold | +2.92% | +2.33% |
| FOLKS/USDT:USDT | below_1h_threshold | +2.80% | +2.21% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

# Decision Report

- generated_at: 2026-05-22T14:34:06.271741+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4707**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4707, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 13/20 | 65.0% | +0.62% | **+0.40%** |
| ASK | 20/20 | 100.0% | +0.39% | **+0.39%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.58% | **+0.35%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.29% | **+0.80%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.07% | **+0.31%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |
| MARKET_LONG | 20/20 | 100.0% | +0.00% | **+0.00%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | -0.20% | **-0.12%** |

## 2. $100 Live Portfolio

- 残高: **$95.25** / 初期 $100.00 (-4.75%)
- 確定トレード: 60件 (TP 15 / SL 42 / EXP 3)
- 最新: STXSTOCK/USDT:USDT SL_HIT PnL -1.86% 残高後 $95.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.66** / 初期 $100.00 (+21.66%)
- 確定: 564件 (Win 144 / Loss 186 / Flat 234) / skip 704件
- 成長率目線: 平均log +0.000348 / 幾何平均 +0.035% per trade / maxDD +4.21%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BUILDONBOB/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.12% 残高後 $121.66

## 4. Latest Market Context

- 更新: 2026-05-22T14:34:03.940993+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.62% price=76780.2
- Funnel: target 768 → liquid 138 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BUILDONBOB/USDT:USDT | +65.10% | $4,411,907.83 |
| BEAT/USDT:USDT | +50.31% | $23,009,434.70 |
| GENIUS/USDT:USDT | +38.78% | $3,648,048.25 |
| ALT/USDT:USDT | +31.53% | $3,286,726.84 |
| AGT/USDT:USDT | +29.03% | $1,018,375.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ARMSTOCK/USDT:USDT | below_1h_threshold | +3.03% | +3.65% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +1.62% | +2.24% |
| TESLA/USDT:USDT | below_1h_threshold | +1.50% | +2.12% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.17% | +1.78% |
| SPOTSTOCK/USDT:USDT | below_1h_threshold | +1.17% | +1.78% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

# Decision Report

- generated_at: 2026-05-22T14:18:15.142751+00:00
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

- 更新: 2026-05-22T14:18:13.469144+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.34% price=76996.4
- Funnel: target 768 → liquid 137 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BUILDONBOB/USDT:USDT | +63.11% | $4,343,462.32 |
| BEAT/USDT:USDT | +60.85% | $21,325,210.29 |
| GENIUS/USDT:USDT | +38.01% | $3,569,951.65 |
| ALT/USDT:USDT | +33.20% | $3,253,735.61 |
| AGT/USDT:USDT | +31.73% | $1,011,041.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BUILDONBOB/USDT:USDT | below_1h_threshold | +4.77% | +5.10% |
| BEAT/USDT:USDT | below_1h_threshold | +3.85% | +4.18% |
| JTO/USDT:USDT | below_1h_threshold | +2.57% | +2.90% |
| AGT/USDT:USDT | below_1h_threshold | +1.77% | +2.11% |
| PEAQ/USDT:USDT | below_1h_threshold | +1.30% | +1.63% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

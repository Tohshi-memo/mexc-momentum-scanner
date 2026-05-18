# Decision Report

- generated_at: 2026-05-18T06:28:30.680580+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4438**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4438, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.03% | **-0.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 3/20 | 15.0% | +0.54% | **+0.08%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.23% | **+0.08%** |
| LIMIT_5PCT | 5/20 | 25.0% | -0.04% | **-0.01%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |
| LIMIT_8PCT | 2/20 | 10.0% | -0.15% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +1.68% | **+1.68%** |
| MARKET_LONG | 20/20 | 100.0% | +1.66% | **+1.66%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.30% | **+0.97%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.11% | **+0.72%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.91% | **+0.59%** |

## 2. $100 Live Portfolio

- 残高: **$96.22** / 初期 $100.00 (-3.78%)
- 確定トレード: 52件 (TP 13 / SL 36 / EXP 3)
- 最新: PLAY/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.22
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$122.63** / 初期 $100.00 (+22.63%)
- 確定: 435件 (Win 114 / Loss 147 / Flat 174) / skip 564件
- 成長率目線: 平均log +0.000469 / 幾何平均 +0.047% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $122.63

## 4. Latest Market Context

- 更新: 2026-05-18T06:28:28.687998+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.22% price=76720.4
- Funnel: target 765 → liquid 129 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| FIDA/USDT:USDT | +42.19% | $6,925,779.52 |
| BSB/USDT:USDT | +12.93% | $20,027,273.30 |
| OPENLEDGER/USDT:USDT | +4.16% | $1,307,679.29 |
| HYPE/USDT:USDT | +3.64% | $277,654,765.32 |
| ZEC/USDT:USDT | +2.93% | $482,111,892.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +3.69% | +3.90% |
| UB/USDT:USDT | below_1h_threshold | +2.22% | +2.44% |
| TONCOIN/USDT:USDT | below_1h_threshold | +0.87% | +1.09% |
| RIVER/USDT:USDT | below_1h_threshold | +0.81% | +1.03% |
| SILVER/USDT:USDT | below_1h_threshold | +0.49% | +0.71% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

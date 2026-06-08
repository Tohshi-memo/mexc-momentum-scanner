# Decision Report

- generated_at: 2026-06-08T11:48:03.202208+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6071**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6071, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 16/20 | 80.0% | +0.25% | **+0.20%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.52% | **+0.18%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.60% | **-0.48%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 11/20 | 55.0% | +3.30% | **+1.81%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.22% | **+1.33%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.03% | **+0.93%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$97.59** / 初期 $100.00 (-2.41%)
- 確定トレード: 9件 (TP 1 / SL 7 / EXP 1)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.59
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.21** / 初期 $100.00 (+51.21%)
- 確定: 1144件 (Win 280 / Loss 350 / Flat 514) / skip 1488件
- 成長率目線: 平均log +0.000361 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $151.21

## 4. Latest Market Context

- 更新: 2026-06-08T11:47:57.837808+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.57% price=63488.9
- Funnel: target 777 → liquid 148 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 95.8 >= 65=1, 4h RSI 91.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BEAT/USDT:USDT | +52.68% | $135,071,062.13 |
| ALLO/USDT:USDT | +50.10% | $64,772,406.13 |
| VELVET/USDT:USDT | +46.27% | $6,256,368.11 |
| PIPPIN/USDT:USDT | +36.45% | $14,681,732.23 |
| BANK/USDT:USDT | +25.07% | $5,557,414.79 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKHYNIXSTOCK/USDT:USDT | below_relative_strength | +5.28% | +4.71% |
| STG/USDT:USDT | below_1h_threshold | +3.59% | +3.03% |
| USELESS/USDT:USDT | below_1h_threshold | +2.82% | +2.25% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +2.42% | +1.85% |
| RAVE/USDT:USDT | below_1h_threshold | +2.13% | +1.56% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

# Decision Report

- generated_at: 2026-06-08T08:21:42.871281+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6060**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6060, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +1.05% | **+0.37%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.97% | **+0.24%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.46% | **+0.23%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.27% | **+0.20%** |
| LIMIT_3PCT | 15/20 | 75.0% | -0.57% | **-0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +3.32% | **+2.16%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.19% | **+1.53%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.32% | **+1.28%** |
| LIMIT_FIB1272_LONG | 4/20 | 20.0% | +5.69% | **+1.14%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +4.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$97.59** / 初期 $100.00 (-2.41%)
- 確定トレード: 9件 (TP 1 / SL 7 / EXP 1)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.59
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.21** / 初期 $100.00 (+51.21%)
- 確定: 1144件 (Win 280 / Loss 350 / Flat 514) / skip 1477件
- 成長率目線: 平均log +0.000361 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $151.21

## 4. Latest Market Context

- 更新: 2026-06-08T08:21:40.094822+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.43% price=62988.0
- Funnel: target 777 → liquid 145 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BEAT/USDT:USDT | +49.28% | $112,584,111.47 |
| ALLO/USDT:USDT | +49.02% | $41,535,053.88 |
| PIPPIN/USDT:USDT | +48.51% | $10,531,687.83 |
| BANK/USDT:USDT | +24.95% | $5,259,090.57 |
| SKYAI/USDT:USDT | +23.34% | $15,329,289.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOME/USDT:USDT | below_1h_threshold | +4.33% | +4.75% |
| SAHARA/USDT:USDT | below_1h_threshold | +3.25% | +3.67% |
| BEAT/USDT:USDT | below_1h_threshold | +3.15% | +3.58% |
| PIPPIN/USDT:USDT | below_1h_threshold | +2.91% | +3.34% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.68% | +2.10% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

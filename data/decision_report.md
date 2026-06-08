# Decision Report

- generated_at: 2026-06-08T09:37:50.169839+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6063**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6063, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 15/20 | 75.0% | +0.27% | **+0.20%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +0.79% | **+0.20%** |
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.33% | **+0.13%** |
| LIMIT_3PCT | 15/20 | 75.0% | -0.57% | **-0.43%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.93% | **+1.76%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.32% | **+1.74%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.66% | **+1.59%** |
| LIMIT_FIB1272_LONG | 4/20 | 20.0% | +5.69% | **+1.14%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +4.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$97.59** / 初期 $100.00 (-2.41%)
- 確定トレード: 9件 (TP 1 / SL 7 / EXP 1)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.59
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.21** / 初期 $100.00 (+51.21%)
- 確定: 1144件 (Win 280 / Loss 350 / Flat 514) / skip 1480件
- 成長率目線: 平均log +0.000361 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $151.21

## 4. Latest Market Context

- 更新: 2026-06-08T09:37:47.665990+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.42% price=63366.0
- Funnel: target 777 → liquid 147 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +55.26% | $47,250,002.46 |
| BEAT/USDT:USDT | +47.94% | $119,593,779.91 |
| PIPPIN/USDT:USDT | +25.15% | $12,501,068.48 |
| BANK/USDT:USDT | +25.10% | $5,440,930.28 |
| BLESS/USDT:USDT | +24.34% | $9,232,604.37 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_relative_strength | +5.35% | +4.93% |
| MYX/USDT:USDT | below_1h_threshold | +3.92% | +3.50% |
| BLESS/USDT:USDT | below_1h_threshold | +3.14% | +2.72% |
| SAHARA/USDT:USDT | below_1h_threshold | +2.75% | +2.33% |
| B/USDT:USDT | below_1h_threshold | +2.19% | +1.77% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

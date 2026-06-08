# Decision Report

- generated_at: 2026-06-08T14:18:59.326518+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6080**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6080, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.53%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.53% | **-1.53%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_7PCT | 2/20 | 10.0% | -0.60% | **-0.06%** |
| LIMIT_6PCT | 2/20 | 10.0% | -1.06% | **-0.11%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | -0.35% | **-0.14%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.27% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.93% | **+1.93%** |
| ASK_LONG | 20/20 | 100.0% | +1.37% | **+1.37%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.82% | **+1.27%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +1.99% | **+0.90%** |
| LIMIT_2PCT_LONG | 8/20 | 40.0% | +1.30% | **+0.52%** |

## 2. $100 Live Portfolio

- 残高: **$97.59** / 初期 $100.00 (-2.41%)
- 確定トレード: 9件 (TP 1 / SL 7 / EXP 1)
- 最新: SKYAI/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.59
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.21** / 初期 $100.00 (+51.21%)
- 確定: 1144件 (Win 280 / Loss 350 / Flat 514) / skip 1497件
- 成長率目線: 平均log +0.000361 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: GUA/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $151.21

## 4. Latest Market Context

- 更新: 2026-06-08T14:18:56.168548+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=63655.8
- Funnel: target 777 → liquid 152 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 96.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +60.07% | $9,669,503.28 |
| ALLO/USDT:USDT | +47.00% | $79,116,702.81 |
| BEAT/USDT:USDT | +44.17% | $151,895,087.16 |
| PIPPIN/USDT:USDT | +38.04% | $15,930,909.39 |
| BLESS/USDT:USDT | +22.88% | $10,452,617.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LUNC/USDT:USDT | below_1h_threshold | +2.93% | +3.04% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +1.41% | +1.52% |
| VVV/USDT:USDT | below_1h_threshold | +1.41% | +1.51% |
| INTCSTOCK/USDT:USDT | below_1h_threshold | +1.10% | +1.21% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +1.05% | +1.16% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

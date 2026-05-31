# Decision Report

- generated_at: 2026-05-31T19:00:22.633707+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5215**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5215, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.81%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.81% | **-1.81%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.91% | **+0.27%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.27% | **+0.22%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.40% | **+0.18%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +4.00% | **+4.00%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.63% | **+1.81%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +3.26% | **+1.47%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.55% | **+1.40%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +4.58% | **+1.38%** |

## 2. $100 Live Portfolio

- 残高: **$98.09** / 初期 $100.00 (-1.91%)
- 確定トレード: 81件 (TP 24 / SL 54 / EXP 3)
- 最新: GUN/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.09
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$128.58** / 初期 $100.00 (+28.58%)
- 確定: 850件 (Win 196 / Loss 253 / Flat 401) / skip 926件
- 成長率目線: 平均log +0.000296 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STG/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $128.58

## 4. Latest Market Context

- 更新: 2026-05-31T19:00:20.395759+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=73580.3
- Funnel: target 773 → liquid 125 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| STG/USDT:USDT | +27.39% | $9,897,298.95 |
| BSB/USDT:USDT | +9.11% | $4,393,916.17 |
| BIANRENSHENG/USDT:USDT | +7.82% | $2,718,748.68 |
| HOME/USDT:USDT | +7.72% | $2,379,384.98 |
| SKYAI/USDT:USDT | +7.50% | $4,787,869.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| HOME/USDT:USDT | below_1h_threshold | +2.46% | +2.45% |
| CHIP/USDT:USDT | below_1h_threshold | +0.57% | +0.56% |
| LAB/USDT:USDT | below_1h_threshold | +0.27% | +0.26% |
| MEME/USDT:USDT | below_1h_threshold | +0.27% | +0.26% |
| XLM/USDT:USDT | below_1h_threshold | +0.20% | +0.19% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

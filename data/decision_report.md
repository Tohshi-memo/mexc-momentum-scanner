# Decision Report

- generated_at: 2026-05-09T06:07:56.591410+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3858**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3858, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.49%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.49% | **-0.49%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 15/20 | 75.0% | +0.71% | **+0.53%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.40% | **+0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 14/20 | 70.0% | +2.06% | **+1.44%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +3.46% | **+1.04%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.35% | **+0.94%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.35% | **+0.94%** |
| MARKET_LONG | 20/20 | 100.0% | +0.85% | **+0.85%** |

## 2. $100 Live Portfolio

- 残高: **$98.71** / 初期 $100.00 (-1.29%)
- 確定トレード: 29件 (TP 7 / SL 19 / EXP 3)
- 最新: LUNC/USDT:USDT EXPIRED PnL +3.11% 残高後 $98.71
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 193件 (Win 48 / Loss 64 / Flat 81) / skip 226件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-09T06:07:53.666474+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=80364.1
- Funnel: target 767 → liquid 173 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DYM/USDT:USDT | +31.24% | $2,045,443.60 |
| ZEREBRO/USDT:USDT | +27.38% | $1,025,940.42 |
| CORE/USDT:USDT | +26.87% | $2,310,621.41 |
| PLUME/USDT:USDT | +19.39% | $1,527,819.24 |
| ICP/USDT:USDT | +17.72% | $217,040,798.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ANTHROPIC/USDT:USDT | below_1h_threshold | +2.05% | +2.00% |
| AERO/USDT:USDT | below_1h_threshold | +1.86% | +1.82% |
| GALA/USDT:USDT | below_1h_threshold | +1.48% | +1.44% |
| ZEREBRO/USDT:USDT | below_1h_threshold | +1.41% | +1.37% |
| SPX/USDT:USDT | below_1h_threshold | +1.23% | +1.18% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

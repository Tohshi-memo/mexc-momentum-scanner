# Decision Report

- generated_at: 2026-05-28T20:44:50.636386+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4992**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4992, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=-0.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.59% | **-0.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | -0.14% | **-0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +3.10% | **+0.93%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.29% | **+0.91%** |
| MARKET_LONG | 20/20 | 100.0% | +0.88% | **+0.88%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.44% | **+0.87%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.70% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$98.61** / 初期 $100.00 (-1.39%)
- 確定トレード: 71件 (TP 21 / SL 47 / EXP 3)
- 最新: BILL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$128.23** / 初期 $100.00 (+28.23%)
- 確定: 726件 (Win 175 / Loss 222 / Flat 329) / skip 827件
- 成長率目線: 平均log +0.000342 / 幾何平均 +0.034% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ETHFI/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $128.23

## 4. Latest Market Context

- 更新: 2026-05-28T20:44:48.457357+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.38% price=73669.6
- Funnel: target 773 → liquid 166 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +35.54% | $10,890,714.38 |
| CLO/USDT:USDT | +21.14% | $1,088,477.52 |
| DELLSTOCK/USDT:USDT | +13.28% | $4,792,640.38 |
| VVV/USDT:USDT | +11.86% | $10,389,364.07 |
| AR/USDT:USDT | +11.68% | $2,058,394.81 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ETHFI/USDT:USDT | below_1h_threshold | +3.49% | +3.11% |
| XLM/USDT:USDT | below_1h_threshold | +2.93% | +2.56% |
| AR/USDT:USDT | below_1h_threshold | +2.89% | +2.51% |
| XPL/USDT:USDT | below_1h_threshold | +2.77% | +2.39% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +2.11% | +1.73% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

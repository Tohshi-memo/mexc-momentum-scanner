# Decision Report

- generated_at: 2026-05-13T03:13:00.843081+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4181**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.21% / filled 20/20。**
- 全期間 MARKET基準: n=4181, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+1.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.21% | **+1.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +2.15% | **+2.04%** |
| LIMIT_2PCT | 15/20 | 75.0% | +2.00% | **+1.50%** |
| MARKET | 20/20 | 100.0% | +1.21% | **+1.21%** |
| LIMIT_ATR | 14/20 | 70.0% | +1.42% | **+1.00%** |
| ASK | 20/20 | 100.0% | +0.96% | **+0.96%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +4.55% | **+0.91%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +2.08% | **+0.83%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | -0.46% | **-0.18%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | -0.47% | **-0.26%** |

## 2. $100 Live Portfolio

- 残高: **$98.69** / 初期 $100.00 (-1.31%)
- 確定トレード: 35件 (TP 9 / SL 23 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -3.91% 残高後 $98.69
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$119.96** / 初期 $100.00 (+19.96%)
- 確定: 317件 (Win 91 / Loss 112 / Flat 114) / skip 425件
- 成長率目線: 平均log +0.000574 / 幾何平均 +0.057% per trade / maxDD +4.21%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: IRYS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $119.96

## 4. Latest Market Context

- 更新: 2026-05-13T03:12:57.692606+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.01% price=81007.4
- Funnel: target 763 → liquid 184 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IRYS/USDT:USDT | +31.74% | $2,920,642.69 |
| PEAQ/USDT:USDT | +20.17% | $2,300,541.94 |
| SATO/USDT:USDT | +13.25% | $1,053,714.71 |
| ARKM/USDT:USDT | +12.86% | $1,047,702.95 |
| TIA/USDT:USDT | +12.67% | $28,237,933.88 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| IRYS/USDT:USDT | below_1h_threshold | +4.44% | +4.45% |
| SATO/USDT:USDT | below_1h_threshold | +1.60% | +1.61% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.00% | +1.01% |
| VELO/USDT:USDT | below_1h_threshold | +0.94% | +0.95% |
| UB/USDT:USDT | below_1h_threshold | +0.82% | +0.83% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

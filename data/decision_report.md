# Decision Report

- generated_at: 2026-06-15T11:42:54.885649+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6774**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6774, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 18/20 | 90.0% | +0.58% | **+0.52%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +2.05% | **+0.41%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.27% | **+0.20%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.81% | **+1.45%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.50% | **+1.27%** |
| ASK_LONG | 20/20 | 100.0% | +1.09% | **+1.09%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.31% | **+0.72%** |
| MARKET_LONG | 20/20 | 100.0% | +0.60% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$103.02** / 初期 $100.00 (+3.02%)
- 確定トレード: 6件 (TP 4 / SL 2 / EXP 0)
- 最新: RIF/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.02
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$176.25** / 初期 $100.00 (+76.25%)
- 確定: 1647件 (Win 430 / Loss 510 / Flat 707) / skip 1688件
- 成長率目線: 平均log +0.000344 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UAI/USDT:USDT `LIMIT_3PCT_LONG` TP_HIT account +1.00% 残高後 $176.25

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.96** / 初期 $100.00 (-1.04%)
- 確定: 141件 (Win 28 / Loss 25 / Flat 88) / skip 44件
- 成長率目線: 平均log -0.000074 / 幾何平均 -0.007% per trade / maxDD +2.18%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_robust_growth_score) / robust_score -0.0204 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: UAI/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.51% 残高後 $98.96

## 5. Latest Market Context

- 更新: 2026-06-15T11:42:50.951001+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.44% price=66172.5
- Funnel: target 771 → liquid 147 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +89.68% | $4,823,980.83 |
| EVAA/USDT:USDT | +85.71% | $29,662,643.21 |
| CLO/USDT:USDT | +39.53% | $2,336,075.70 |
| UAI/USDT:USDT | +32.39% | $2,987,872.56 |
| ZEC/USDT:USDT | +26.35% | $250,634,411.89 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZEC/USDT:USDT | below_relative_strength | +5.04% | +4.61% |
| WLD/USDT:USDT | below_1h_threshold | +4.10% | +3.66% |
| USELESS/USDT:USDT | below_1h_threshold | +3.40% | +2.96% |
| XPL/USDT:USDT | below_1h_threshold | +3.27% | +2.83% |
| ZRO/USDT:USDT | below_1h_threshold | +3.12% | +2.68% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

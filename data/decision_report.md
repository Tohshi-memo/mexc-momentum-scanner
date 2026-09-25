# Decision Report

- generated_at: 2026-09-25T10:31:32.415134+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15518**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15518, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.57% | **-0.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 10/20 | 50.0% | +2.57% | **+1.29%** |
| LIMIT_6PCT | 6/20 | 30.0% | +3.92% | **+1.18%** |
| LIMIT_8PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_3PCT | 15/20 | 75.0% | +1.01% | **+0.76%** |
| LIMIT_7PCT | 2/20 | 10.0% | +5.40% | **+0.54%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +3.08% | **+1.54%** |
| LIMIT_BB3S_LONG | 7/9 | 77.8% | +1.21% | **+0.94%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.32% | **+0.79%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +0.84% | **+0.67%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.88% | **+0.66%** |

## 2. $100 Live Portfolio

- 残高: **$120.08** / 初期 $100.00 (+20.08%)
- 確定トレード: 219件 (TP 79 / SL 135 / EXP 5)
- 最新: XPL/USDT:USDT SL_HIT PnL -3.85% 残高後 $120.08
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,206.94** / 初期 $100.00 (+1106.94%)
- 確定: 5901件 (Win 1740 / Loss 1890 / Flat 2271) / skip 6178件
- 成長率目線: 平均log +0.000422 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PHA/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.76% 残高後 $1,206.94

## 4. Robust Adaptive DryRun ($100)

- 残高: **$254.57** / 初期 $100.00 (+154.57%)
- 確定: 3451件 (Win 951 / Loss 793 / Flat 1707) / skip 5478件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0160 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: XPL/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $254.57

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.91** / 初期 $100.00 (+19.91%)
- 確定: 3171件 (Win 933 / Loss 1255 / Flat 983) / pending 0件 / skip 3820件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000161 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: XPL/USDT:USDT `MARKET` EXPIRED account -0.07% 残高後 $119.91

## 6. Latest Market Context

- 更新: 2026-09-25T10:31:19.336239+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=84719.0
- Funnel: target 1069 → liquid 175 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARK/USDT:USDT | +25.92% | $1,377,213.06 |
| PHA/USDT:USDT | +20.69% | $2,155,980.20 |
| QNT/USDT:USDT | +19.90% | $14,492,230.72 |
| GRASS/USDT:USDT | +16.16% | $1,117,725.17 |
| SYN/USDT:USDT | +13.78% | $3,557,644.21 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NIL/USDT:USDT | below_1h_threshold | +4.49% | +4.26% |
| ARK/USDT:USDT | below_1h_threshold | +4.33% | +4.11% |
| QNT/USDT:USDT | below_1h_threshold | +2.69% | +2.46% |
| FET/USDT:USDT | below_1h_threshold | +2.63% | +2.41% |
| CHIP/USDT:USDT | below_1h_threshold | +2.17% | +1.95% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

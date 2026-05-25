# Decision Report

- generated_at: 2026-05-25T03:14:15.917347+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4841**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4841, expectancy=-0.08%
- 直近20件 MARKET基準: n=20, expectancy=+0.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.12% | **+0.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.68% | **+0.34%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| ASK | 20/20 | 100.0% | +0.20% | **+0.20%** |
| MARKET | 20/20 | 100.0% | +0.12% | **+0.12%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +0.81% | **+0.81%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.81% | **+0.53%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.54% | **+0.19%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.22% | **+0.12%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +1.10% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$96.68** / 初期 $100.00 (-3.32%)
- 確定トレード: 63件 (TP 17 / SL 43 / EXP 3)
- 最新: KITE/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.68
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.26** / 初期 $100.00 (+23.26%)
- 確定: 647件 (Win 160 / Loss 206 / Flat 281) / skip 755件
- 成長率目線: 平均log +0.000323 / 幾何平均 +0.032% per trade / maxDD +4.72%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: XAN/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.71% 残高後 $123.26

## 4. Latest Market Context

- 更新: 2026-05-25T03:14:13.782960+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=77034.4
- Funnel: target 764 → liquid 113 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| XAN/USDT:USDT | +24.06% | $1,597,584.35 |
| SPORTFUN/USDT:USDT | +12.81% | $1,187,464.55 |
| H/USDT:USDT | +5.42% | $1,020,870.61 |
| SAGA/USDT:USDT | +4.61% | $1,213,558.07 |
| SUPER/USDT:USDT | +3.73% | $3,319,986.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| QNT/USDT:USDT | below_1h_threshold | +1.12% | +1.16% |
| SPORTFUN/USDT:USDT | below_1h_threshold | +0.90% | +0.94% |
| BEAT/USDT:USDT | below_1h_threshold | +0.74% | +0.77% |
| SAGA/USDT:USDT | below_1h_threshold | +0.61% | +0.64% |
| CHIP/USDT:USDT | below_1h_threshold | +0.50% | +0.54% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

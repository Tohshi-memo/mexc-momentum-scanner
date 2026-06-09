# Decision Report

- generated_at: 2026-06-09T11:04:39.611574+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6130**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6130, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.39%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.39% | **-0.39%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +4.64% | **+0.46%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.84% | **+0.43%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.75% | **+0.38%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.44% | **+0.09%** |
| LIMIT_5PCT | 9/20 | 45.0% | -0.14% | **-0.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.87% | **+1.12%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.00% | **+1.00%** |
| ASK_LONG | 20/20 | 100.0% | +0.53% | **+0.53%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.82% | **+0.53%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.42% | **+0.32%** |

## 2. $100 Live Portfolio

- 残高: **$96.62** / 初期 $100.00 (-3.38%)
- 確定トレード: 11件 (TP 1 / SL 9 / EXP 1)
- 最新: SLX/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.62
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$154.20** / 初期 $100.00 (+54.20%)
- 確定: 1170件 (Win 294 / Loss 362 / Flat 514) / skip 1521件
- 成長率目線: 平均log +0.000370 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PLAY/USDT:USDT `MARKET_LONG` TP_HIT account +1.00% 残高後 $154.20

## 4. Latest Market Context

- 更新: 2026-06-09T11:04:36.364475+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.28% price=62571.4
- Funnel: target 774 → liquid 149 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +57.38% | $20,818,319.87 |
| SLX/USDT:USDT | +27.06% | $4,879,722.41 |
| PLAY/USDT:USDT | +20.69% | $1,359,969.44 |
| POWER/USDT:USDT | +17.38% | $2,417,696.71 |
| SKHYNIXSTOCK/USDT:USDT | +10.84% | $4,325,596.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +3.12% | +3.40% |
| BSB/USDT:USDT | below_1h_threshold | +2.84% | +3.12% |
| CTR/USDT:USDT | below_1h_threshold | +1.33% | +1.62% |
| FOLKS/USDT:USDT | below_1h_threshold | +1.10% | +1.39% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +0.53% | +0.81% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

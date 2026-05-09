# Decision Report

- generated_at: 2026-05-09T00:47:41.976638+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3830**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3830, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-0.53%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.53% | **-0.53%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 14/20 | 70.0% | +1.16% | **+0.81%** |
| LIMIT_BB3S | 6/18 | 33.3% | +1.59% | **+0.53%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.54% | **+0.43%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.35% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.69% | **+1.02%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.06% | **+0.74%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +1.08% | **+0.54%** |
| ASK_LONG | 20/20 | 100.0% | +0.52% | **+0.52%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +1.04% | **+0.47%** |

## 2. $100 Live Portfolio

- 残高: **$98.33** / 初期 $100.00 (-1.67%)
- 確定トレード: 28件 (TP 7 / SL 19 / EXP 2)
- 最新: IO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.33
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 193件 (Win 48 / Loss 64 / Flat 81) / skip 198件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +3.48%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BILL/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $108.41

## 4. Latest Market Context

- 更新: 2026-05-09T00:47:38.577424+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.02% price=80171.2
- Funnel: target 767 → liquid 180 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 82.5 >= 65=1, 4h RSI 78.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COLLECT/USDT:USDT | +20.80% | $6,088,183.23 |
| AKT/USDT:USDT | +15.43% | $1,680,974.56 |
| ICP/USDT:USDT | +15.37% | $230,184,135.61 |
| BILL/USDT:USDT | +14.52% | $18,794,924.71 |
| CORE/USDT:USDT | +13.77% | $1,724,429.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONDO/USDT:USDT | below_1h_threshold | +4.81% | +4.79% |
| SUI/USDT:USDT | below_1h_threshold | +4.67% | +4.65% |
| H/USDT:USDT | below_1h_threshold | +4.44% | +4.42% |
| SEI/USDT:USDT | below_1h_threshold | +2.72% | +2.70% |
| BILL/USDT:USDT | below_1h_threshold | +2.71% | +2.69% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

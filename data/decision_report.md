# Decision Report

- generated_at: 2026-05-28T20:29:40.612656+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4991**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4991, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=-0.01%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.01% | **-0.01%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.28% | **+0.27%** |
| LIMIT_8PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +3.80% | **+1.33%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +2.92% | **+1.31%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +4.13% | **+0.83%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.02% | **+0.67%** |

## 2. $100 Live Portfolio

- 残高: **$98.61** / 初期 $100.00 (-1.39%)
- 確定トレード: 71件 (TP 21 / SL 47 / EXP 3)
- 最新: BILL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$128.23** / 初期 $100.00 (+28.23%)
- 確定: 725件 (Win 175 / Loss 222 / Flat 328) / skip 827件
- 成長率目線: 平均log +0.000343 / 幾何平均 +0.034% per trade / maxDD +4.72%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $128.23

## 4. Latest Market Context

- 更新: 2026-05-28T20:29:38.082656+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.34% price=73637.6
- Funnel: target 773 → liquid 166 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ALLO/USDT:USDT | +41.44% | $10,219,109.03 |
| CLO/USDT:USDT | +22.14% | $1,048,499.94 |
| DELLSTOCK/USDT:USDT | +14.16% | $4,681,066.97 |
| XPL/USDT:USDT | +11.25% | $3,864,877.22 |
| AR/USDT:USDT | +10.38% | $2,023,589.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALLO/USDT:USDT | below_relative_strength | +5.27% | +4.93% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +2.78% | +2.44% |
| XPL/USDT:USDT | below_1h_threshold | +2.13% | +1.79% |
| ETHFI/USDT:USDT | below_1h_threshold | +1.90% | +1.57% |
| AR/USDT:USDT | below_1h_threshold | +1.69% | +1.36% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

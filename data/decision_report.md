# Decision Report

- generated_at: 2026-06-08T01:38:18.115112+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6016**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6016, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=-2.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.17% | **-2.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.34% | **+0.40%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_BB3S | 2/16 | 12.5% | +1.81% | **+0.23%** |
| LIMIT_4PCT | 17/20 | 85.0% | +0.03% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 20/20 | 100.0% | +2.06% | **+2.06%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +2.32% | **+1.51%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.81% | **+1.36%** |
| ASK_LONG | 20/20 | 100.0% | +1.26% | **+1.26%** |
| MARKET_LONG | 20/20 | 100.0% | +1.23% | **+1.23%** |

## 2. $100 Live Portfolio

- 残高: **$99.07** / 初期 $100.00 (-0.93%)
- 確定トレード: 6件 (TP 1 / SL 4 / EXP 1)
- 最新: LUNC/USDT:USDT EXPIRED PnL +0.53% 残高後 $99.07
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$154.26** / 初期 $100.00 (+54.26%)
- 確定: 1133件 (Win 277 / Loss 343 / Flat 513) / skip 1444件
- 成長率目線: 平均log +0.000383 / 幾何平均 +0.038% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $154.26

## 4. Latest Market Context

- 更新: 2026-06-08T01:38:15.029724+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.97% price=62981.9
- Funnel: target 773 → liquid 142 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 88.6 >= 65=1, 4h RSI 67.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BEAT/USDT:USDT | +32.76% | $88,469,550.42 |
| BANK/USDT:USDT | +32.16% | $4,580,300.42 |
| BLESS/USDT:USDT | +31.87% | $7,818,095.29 |
| PIPPIN/USDT:USDT | +20.67% | $6,324,207.13 |
| EPIC/USDT:USDT | +20.38% | $1,503,945.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +4.35% | +5.32% |
| BEAT/USDT:USDT | below_1h_threshold | +3.56% | +4.54% |
| BANK/USDT:USDT | below_1h_threshold | +3.32% | +4.30% |
| OPENAI/USDT:USDT | below_1h_threshold | +2.00% | +2.97% |
| USOIL/USDT:USDT | below_1h_threshold | +1.58% | +2.55% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

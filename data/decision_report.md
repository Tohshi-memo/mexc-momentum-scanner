# Decision Report

- generated_at: 2026-05-28T17:15:11.983626+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4979**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4979, expectancy=-0.07%
- 直近20件 MARKET基準: n=20, expectancy=-0.91%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.91% | **-0.91%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +4.94% | **+0.99%** |
| LIMIT_7PCT | 3/20 | 15.0% | +6.27% | **+0.94%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.70% | **+0.68%** |
| LIMIT_BB3S | 8/11 | 72.7% | +0.07% | **+0.05%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.51% | **+1.50%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.84% | **+1.20%** |
| LIMIT_BB3S_LONG | 8/9 | 88.9% | +1.14% | **+1.02%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.15% | **+0.92%** |
| LIMIT_6PCT_LONG | 6/20 | 30.0% | +2.86% | **+0.86%** |

## 2. $100 Live Portfolio

- 残高: **$98.61** / 初期 $100.00 (-1.39%)
- 確定トレード: 71件 (TP 21 / SL 47 / EXP 3)
- 最新: BILL/USDT:USDT TP_HIT PnL +8.00% 残高後 $98.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$128.69** / 初期 $100.00 (+28.69%)
- 確定: 714件 (Win 174 / Loss 221 / Flat 319) / skip 826件
- 成長率目線: 平均log +0.000353 / 幾何平均 +0.035% per trade / maxDD +4.72%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HBAR/USDT:USDT `LIMIT_8PCT_LONG` EXPIRED account +0.00% 残高後 $128.69

## 4. Latest Market Context

- 更新: 2026-05-28T17:15:09.297078+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=73441.3
- Funnel: target 776 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +17.78% | $6,680,966.38 |
| ALLO/USDT:USDT | +10.35% | $2,197,654.58 |
| XLM/USDT:USDT | +7.74% | $297,262,421.04 |
| BSB/USDT:USDT | +5.55% | $12,802,389.72 |
| ETHFI/USDT:USDT | +5.24% | $3,189,615.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XLM/USDT:USDT | below_1h_threshold | +4.58% | +4.54% |
| BSB/USDT:USDT | below_1h_threshold | +3.73% | +3.70% |
| XPL/USDT:USDT | below_1h_threshold | +3.58% | +3.55% |
| RIVER/USDT:USDT | below_1h_threshold | +2.76% | +2.73% |
| AR/USDT:USDT | below_1h_threshold | +2.20% | +2.17% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。

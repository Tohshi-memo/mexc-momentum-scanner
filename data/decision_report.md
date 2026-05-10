# Decision Report

- generated_at: 2026-05-10T00:52:50.604410+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3930**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3930, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=+0.07%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.07% | **+0.07%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.72% | **+0.72%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.27% | **+0.22%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.17% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.46% | **+1.35%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.79% | **+0.90%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.91% | **+0.86%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +0.95% | **+0.67%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.61% | **+0.37%** |

## 2. $100 Live Portfolio

- 残高: **$98.21** / 初期 $100.00 (-1.79%)
- 確定トレード: 30件 (TP 7 / SL 20 / EXP 3)
- 最新: SATO/USDT:USDT SL_HIT PnL -4.00% 残高後 $98.21
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$107.73** / 初期 $100.00 (+7.73%)
- 確定: 196件 (Win 48 / Loss 66 / Flat 82) / skip 295件
- 成長率目線: 平均log +0.000380 / 幾何平均 +0.038% per trade / maxDD +4.09%
- 次の候補: `LIMIT_5PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAB/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $107.73

## 4. Latest Market Context

- 更新: 2026-05-10T00:52:44.953058+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=80615.1
- Funnel: target 769 → liquid 174 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 94.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| INX/USDT:USDT | +46.23% | $10,491,559.38 |
| BILL/USDT:USDT | +16.70% | $39,478,648.24 |
| SATO/USDT:USDT | +16.58% | $5,589,056.10 |
| JASMY/USDT:USDT | +14.39% | $16,135,717.86 |
| BANK/USDT:USDT | +12.88% | $1,195,039.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +3.42% | +3.45% |
| BILL/USDT:USDT | below_1h_threshold | +3.05% | +3.07% |
| PHAROS/USDT:USDT | below_1h_threshold | +2.00% | +2.02% |
| KITE/USDT:USDT | below_1h_threshold | +1.66% | +1.68% |
| NIL/USDT:USDT | below_1h_threshold | +1.62% | +1.64% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
